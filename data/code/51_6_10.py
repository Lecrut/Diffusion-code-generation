import argparse

def validate_side_lengths(side_lengths):
    if not all(isinstance(length, (int, float)) and length > 0 for length in side_lengths):
        raise ValueError("All side lengths must be positive numbers.")

def calculate_perimeter(side_lengths):
    if not side_lengths:
        return 0
    validate_side_lengths(side_lengths)
    return sum(side_lengths)

if __name__ == '__main__':
    sample1 = [3, 4, 5]
    sample2 = []
    sample3 = [10, 20, 30, 40]
    sample4 = [7]

    print(f"Perimeter of {sample1}: {calculate_perimeter(sample1)}")
    print(f"Perimeter of {sample2}: {calculate_perimeter(sample2)}")
    print(f"Perimeter of {sample3}: {calculate_perimeter(sample3)}")
    print(f"Perimeter of {sample4}: {calculate_perimeter(sample4)}")