from typing import Any

def are_different(a: Any, b: Any) -> bool:
    return a != b

if __name__ == '__main__':
    sample1 = 42
    sample2 = "42"
    print(are_different(sample1, sample2))