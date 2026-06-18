from typing import Callable

def compare(x: int | float) -> Callable[[int | float], bool]:
    """Returns a lambda that checks if x > y."""
    return (lambda y: x > y)  # type: ignore[operator-missing]

if __name__ == "__main__":
    result = compare(10)(5)