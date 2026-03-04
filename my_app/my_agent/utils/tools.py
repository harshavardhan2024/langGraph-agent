from langchain.tools import tool
from langchain.chat_models import init_chat_model


model = init_chat_model(
    "microsoft/Phi-3-mini-4k-instruct",
    model_provider="huggingface",
    temperature=0.7,
    max_tokens=1024,
)

# Tool Defination 
@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers."""
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Adds two numbers."""
    print("Adding", a, "and", b)
    return a + b

@tool
def subtract(a: int, b: int) -> int:
    """Subtracts two numbers."""
    return a - b

@tool
def divide(a: int, b: int) -> int:
    """Divides two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Arguement thhe LLM with tools
tools = [add, add, subtract, divide]
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)