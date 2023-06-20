import enum

from pydantic import BaseModel, Field

from autogpt.core.resource.model_providers.schema import (
    LanguageModelMessage,
    LanguageModelFunction,
    LanguageModelProviderModelResponse,
)


class LanguageModelClassification(str, enum.Enum):
    """The LanguageModelClassification is a functional description of the model.

    This is used to determine what kind of model to use for a given prompt.
    Sometimes we prefer a faster or cheaper model to accomplish a task when
    possible.

    """

    FAST_MODEL: str = "fast_model"
    SMART_MODEL: str = "smart_model"


class LanguageModelPrompt(BaseModel):
    messages: list[LanguageModelMessage]
    functions: list[LanguageModelFunction] = Field(default_factory=list)

    def __str__(self):
        return "\n\n".join([f"{m.role.value}: {m.content}" for m in self.messages])


class LanguageModelResponse(LanguageModelProviderModelResponse):
    """Standard response struct for a response from a language model."""
