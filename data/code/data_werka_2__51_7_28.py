def calculate_perimeter(sides):
    def validate_side(side):
        if not isinstance(side, (int, float)):
            raise ValueError("All sides must be numeric")
    
    for side in sides:
        validate_side(side)
    
    return sum(sides)

if __name__ == '__main__':
    sample_sides = [8, 15, 17]
    try:
        print(calculate_perimeter(sample_sides))
    except ValueError as e:
        print(e)