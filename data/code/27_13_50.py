from typing import Any

def are_different(a: Any, b: Any) -> bool:
    return not (a == b)

if __name__ == '__main__':
    SAMPLE_INT_1 = 42
    SAMPLE_INT_2 = 84
    SAMPLE_STR_1 = "hello"
    SAMPLE_STR_2 = "world"
    SAMPLE_LIST_1 = [1, 2, 3]
    SAMPLE_LIST_2 = [1, 2, 3]
    SAMPLE_FLOAT_1 = 3.14
    SAMPLE_FLOAT_2 = 3.140000001

    print(are_different(SAMPLE_INT_1, SAMPLE_INT_2))
    print(are_different(SAMPLE_STR_1, SAMPLE_STR_2))
    print(are_different(SAMPLE_LIST_1, SAMPLE_LIST_2))
    print(are_different(SAMPLE_FLOAT_1, SAMPLE_FLOAT_2))