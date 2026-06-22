def calculate_perimeter(sides):
    numeric_check = lambda x: isinstance(x, (int, float))
    if not all(map(numeric_check, sides)):
        raise ValueError("All sides must be numeric")
    perimeter = sum(sides)
    return perimeter

if __name__ == '__main__':
    sample_sides = [8, 15, 17]
    try:
        result = calculate_perimeter(sample_sides)
        print(result)
    except ValueError as e:
        print(e)