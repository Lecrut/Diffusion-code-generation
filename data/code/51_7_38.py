def calculate_perimeter(sides):
    def is_valid_side(side):
        return isinstance(side, (int, float))
    
    if not all(is_valid_side(side) for side in sides):
        raise ValueError("All sides must be numeric")
    
    return sum(sides)

if __name__ == '__main__':
    sample_sides = [6, 8, 10]
    try:
        print(calculate_perimeter(sample_sides))
    except ValueError as e:
        print(e)