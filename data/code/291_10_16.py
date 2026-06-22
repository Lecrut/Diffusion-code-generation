from typing import Optional

def compare_meters(length1: float, length2: float) -> Optional[float]:
    if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
        return None
    if length1 > length2:
        return length1
    elif length2 > length1:
        return length2
    else:
        return None
if __name__ == '__main__':
    result1 = compare_meters(5.0, 3.0)
    print(result1)
    result2 = compare_meters(2.5, 4.5)
    print(result2)