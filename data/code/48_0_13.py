def validate_dimensions(base, height):
    return base > 0 and height > 0

def calculate_area(base, height):
    if not validate_dimensions(base, height):
        return "Invalid dimensions: Base and height must be positive numbers."
    return base * height

if __name__ == '__main__':
    base = 8
    height = 6
    area = calculate_area(base, height)
    print(area)