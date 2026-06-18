def length_difference(len1: int, len2: int) -> int:
    return max(0, len1 - len2) if isinstance(len1, (int | float)) and isinstance(len2, (int | float)) else 0

if __name__ == '__main__':
    result = length_difference(5, 3)
    print(result)