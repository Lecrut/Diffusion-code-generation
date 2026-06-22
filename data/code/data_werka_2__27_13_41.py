from typing import Any

def are_different(a: Any, b: Any) -> bool:
    return not (a == b)

if __name__ == '__main__':
    SAMPLE_1 = 42
    SAMPLE_2 = "42"
    print(are_different(SAMPLE_1, SAMPLE_2))

    SAMPLE_3 = [1, 2, 3]
    SAMPLE_4 = [1, 2, 3]
    print(are_different(SAMPLE_3, SAMPLE_4))

    SAMPLE_5 = None
    SAMPLE_6 = None
    print(are_different(SAMPLE_5, SAMPLE_6))

    SAMPLE_7 = 3.14
    SAMPLE_8 = 3.140000001
    print(are_different(SAMPLE_7, SAMPLE_8))