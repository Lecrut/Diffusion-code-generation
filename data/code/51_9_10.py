def calculate_perimeter(sides):
    if not all(isinstance(side, (int, float)) for side in sides):
        raise ValueError("All sides must be numeric")
    if any(side < 0 for side in sides):
        raise ValueError("All sides must be non-negative")
    
    perimeter = sum(sides)
    return perimeter

if __name__ == '__main__':
    try:
        sample_sides = [3, 4, 5]
        result = calculate_perimeter(sample_sides)
        print(f"The perimeter of the shape with sides {sample_sides} is: {result}")
    except ValueError as e:
        print(e)