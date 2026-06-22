CONVERSION_FACTOR_CM_TO_M = 100

def compare_lengths(length1: float, length2: float) -> str:
    if length1 < length2:
        return f"{length1} cm"
    elif length1 > length2:
        return f"{length2} cm"
    else:
        return "Equal lengths"

if __name__ == '__main__':
    print(compare_lengths(50, 75))
    print(compare_lengths(100, 80))
    print(compare_lengths(100, 100))