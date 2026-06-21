from typing import Any

def are_different(a: Any, b: Any) -> bool:
    return not (a == b)

if __name__ == '__main__':
    sample1 = 42
    sample2 = "42"
    print(are_different(sample1, sample2))

    value1 = [1, 2, 3]
    value2 = [1, 2, 3]
    print(are_different(value1, value2))

    value3 = None
    value4 = None
    print(are_different(value3, value4))

    value5 = 3.0
    value6 = 3
    print(are_different(value5, value6))