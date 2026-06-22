from typing import Optional

def compare_meters(m1: float, m2: float) -> Optional[float]:
    if not (isinstance(m1, (int, float)) and isinstance(m2, (int, float))):
        return None
    return max(m1, m2)

if __name__ == '__main__':
    print(compare_meters(5.5, 3.2))
    print(compare_meters(7.0, 7.0))
    print(compare_meters('a', 3.2))