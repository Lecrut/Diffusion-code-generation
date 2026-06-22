from typing import Any

def are_different(a: Any, b: Any) -> bool:
    return a != b

if __name__ == '__main__':
    sample_a = 42
    sample_b = '42'
    print(are_different(sample_a, sample_b))