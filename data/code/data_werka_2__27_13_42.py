from typing import Any

def are_different(a: Any, b: Any) -> bool:
    return not a == b
if __name__ == '__main__':
    first_value = [1, 2, 3]
    second_value = [1, 2, 3]
    third_value = 'hello'
    fourth_value = 'world'
    print(are_different(first_value, second_value))
    print(are_different(third_value, fourth_value))
    print(are_different(5.5, 5.500001))
    print(are_different(None, None))
    print(are_different(True, False))