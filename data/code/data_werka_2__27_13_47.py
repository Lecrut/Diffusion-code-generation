from typing import Any

def are_different(a: Any, b: Any) -> bool:
    try:
        return not (a == b)
    except Exception as e:
        raise ValueError(f"Comparison failed due to an error: {e}")

if __name__ == '__main__':
    sample1 = 42
    sample2 = "42"
    print(are_different(sample1, sample2))

    sample3 = [1, 2, 3]
    sample4 = [1, 2, 3]
    print(are_different(sample3, sample4))

    sample5 = None
    sample6 = None
    print(are_different(sample5, sample6))

    sample7 = 3.14
    sample8 = 3.140000001
    print(are_different(sample7, sample8))