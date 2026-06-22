from typing import Any

def are_different(a: Any, b: Any) -> bool:
    return not (a == b)

if __name__ == '__main__':
    value1 = 10
    value2 = "10"
    print(are_different(value1, value2))

    value3 = [1, 2, 3]
    value4 = [1, 2, 3]
    print(are_different(value3, value4))

    value5 = None
    value6 = None
    print(are_different(value5, value6))

    value7 = 3.14
    value8 = 3.140000001
    print(are_different(value7, value8))