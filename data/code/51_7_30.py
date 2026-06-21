def calculate_perimeter(sides):
    def validate_sides(sides_list):
        for side in sides_list:
            if not isinstance(side, (int, float)):
                raise ValueError("All sides must be numeric")
    
    validate_sides(sides)
    return sum(sides)

if __name__ == '__main__':
    sample_sides = [8, 15, 17]
    try:
        print(calculate_perimeter(sample_sides))
    except ValueError as e:
        print(e)