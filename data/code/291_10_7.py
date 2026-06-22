def compare_meters(m1: float, m2: float) -> float:
    if not (isinstance(m1, (int, float)) and isinstance(m2, (int, float))):
        return None
    return max(m1, m2)

if __name__ == '__main__':
    print(compare_meters(5.0, 3.5))
    print(compare_meters(7.2, 7.2))
    print(compare_meters('a', 3.5))