def compare_meters(m1: float, m2: float) -> float:
    if not (isinstance(m1, (int, float)) and isinstance(m2, (int, float))):
        return None
    return max(m1, m2)

if __name__ == '__main__':
    length1 = 5.7
    length2 = 3.4
    longer_length = compare_meters(length1, length2)
    print(f"The longer length is: {longer_length}")