def validate_side_lengths(side_lengths):
    if not all(isinstance(length, (int, float)) and length > 0 for length in side_lengths):
        raise ValueError("All side lengths must be positive numbers")

def calculate_perimeter(side_lengths):
    validate_side_lengths(side_lengths)
    return sum(side_lengths)

if __name__ == '__main__':
    sample_sides = [5, 3, 4, 2]
    perimeter = calculate_perimeter(sample_sides)
    print(perimeter)