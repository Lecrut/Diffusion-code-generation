def calculate_perimeter(sides):
    if not all(isinstance(side, (int, float)) for side in sides):
        raise ValueError("All sides must be numeric")
    return sum(sides)

if __name__ == '__main__':
    sample_sides1 = [3, 4, 5]
    try:
        print(calculate_perimeter(sample_sides1))
    except ValueError as e:
        print(e)
    
    sample_sides2 = [7, 24, 25]
    try:
        print(calculate_perimeter(sample_sides2))
    except ValueError as e:
        print(e)