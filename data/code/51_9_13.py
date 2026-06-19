def is_valid_length(length):
    return isinstance(length, (int, float)) and length >= 0

def calculate_perimeter(sides):
    if not all(is_valid_length(side) for side in sides):
        raise ValueError("All sides must be non-negative numbers")
    return sum(sides)

if __name__ == '__main__':
    sample_sides = [3, 4, 5]
    print(calculate_perimeter(sample_sides))