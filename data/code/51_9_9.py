def calculate_perimeter(sides):
    if not all(isinstance(side, (int, float)) for side in sides):
        raise ValueError("All elements in the list must be numeric.")
    return sum(sides)

if __name__ == '__main__':
    sample_sides = [3, 4, 5]
    try:
        perimeter = calculate_perimeter(sample_sides)
        print(perimeter)
    except ValueError as e:
        print(e)