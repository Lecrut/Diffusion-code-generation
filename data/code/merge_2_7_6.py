from dataclasses import dataclass
@dataclass(frozen=True)
class Condition:
    value: bool | None = None
    operator: str = "eq"
def evaluate(condition: Condition) -> tuple[bool, Exception]:
    if condition.value is not None and (condition.operator == "eq"):
        return True, None
    raise ValueError("Invalid configuration")
if __name__ == '__main__':
    c1 = Condition(value=True, operator="eq")
    result, error = evaluate(c1)
    print(f"Result: {result}, Error: {error}")
    try:
        c2 = Condition(value=None, operator="neq")
        _evaluate(c2)
    except Exception as e:
        print(f"Caught exception type: {type(e).__name__}")