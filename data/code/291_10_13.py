from typing import Optional

def compare_lengths(length1: float, length2: float) -> Optional[float]:
    if not (isinstance(length1, (int, float)) and isinstance(length2, (int, float))):
        return None
    return max(length1, length2)

if __name__ == '__main__':
    print(compare_lengths(5.5, 3.2))
    print(compare_lengths(7.0, 7.0))
    print(compare_lengths('a', 5.5))