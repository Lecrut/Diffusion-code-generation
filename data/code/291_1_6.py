def compare_lengths(length1: float, length2: float) -> str:
    if length1 < length2:
        return f"{length1} cm"
    else:
        return f"{length2} cm"

if __name__ == '__main__':
    print(compare_lengths(50, 75))
    print(compare_lengths(100, 80))