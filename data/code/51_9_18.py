def calculate_perimeter(sides):
    if not all(isinstance(side, (int, float)) for side in sides):
        raise ValueError("All sides must be numeric")
    if any(side < 0 for side in sides):
        raise ValueError("Sides must be non-negative")
    
    perimeter = sum(sides)
    return perimeter

if __name__ == '__main__':
    sample_sides = [3.5, 4.2, 6.8]
    try:
        result = calculate_perimeter(sample_sides)
        print(result)
    except ValueError as e:
        print(e)