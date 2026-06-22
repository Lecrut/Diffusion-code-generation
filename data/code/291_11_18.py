def compare_lengths(length1: float, length2: float) -> float:
    if not (isinstance(length1, (int, float)) and isinstance(length2, (int, float))):
        raise ValueError("Both inputs must be numeric values.")
    return max(length1, length2)

if __name__ == '__main__':
    print(f"{compare_lengths(5.75, 3.25):.2f}")
    print(f"{compare_lengths(8.0, 10.5):.2f}")