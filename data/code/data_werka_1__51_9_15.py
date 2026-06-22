def calculate_perimeter(sides):
    if not all(isinstance(side, (int, float)) and side >= 0 for side in sides):
        raise ValueError("All sides must be non-negative numbers")
    return sum(sides)

if __name__ == '__main__':
    try:
        sample_values = [3, 4, 5]
        print(calculate_perimeter(sample_values))
    except ValueError as e:
        print(e)