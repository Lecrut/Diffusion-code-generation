def calculate_perimeter(sides):
    def is_numeric(value):
        return isinstance(value, (int, float))
    
    if not all(is_numeric(side) for side in sides):
        raise ValueError("All sides must be numeric")
    
    return sum(sides)

if __name__ == '__main__':
    sample_sides = [5, 12, 13]
    try:
        print(calculate_perimeter(sample_sides))
    except ValueError as e:
        print(e)