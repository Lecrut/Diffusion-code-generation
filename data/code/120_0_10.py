from typing import Any

def values_match(x: Any, y: Any) -> bool:
    return x == y
if __name__ == '__main__':
    sample1 = 7
    sample2 = '7'
    result1 = values_match(sample1, sample1)
    result2 = values_match(sample1, sample2)
    print(result1)
    print(result2)