def calculate_ratio(length1: float, length2: float) -> None:
    """Calculates and prints the ratio of two lengths."""
    if length2 == 0:
        print(f"Error: Division by zero in calculation for {length1} / {length2}")
        return

    ratio = length1 / length2
    print(f"The ratio of {length1} to {length2} is {ratio:.4f}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or arguments)
    length_a = 10.5
    length_b = 3

    calculate_ratio(length_a, length_b)