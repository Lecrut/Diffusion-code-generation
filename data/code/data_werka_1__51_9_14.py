def calculate_perimeter(sides):
    if not all(isinstance(side, (int, float)) for side in sides):
        raise ValueError("All sides must be numeric")
    if any(side < 0 for side in sides):
        raise ValueError("All sides must be non-negative")
    return sum(sides)

if __name__ == '__main__':
    sample_values = [3, 4, 5]
    print(calculate_perimeter(sample_values))