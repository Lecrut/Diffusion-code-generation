def validate_height(height):
    if not isinstance(height, int):
        raise TypeError("Height must be an integer")
    if height <= 0:
        raise ValueError("Height must be positive")
    return height

def generate_triangle_lines(height):
    valid_height = validate_height(height)
    lines = []
    for current_level in range(1, valid_height + 1):
        line = '*' * current_level
        lines.append(line)
    return lines

def print_triangle(height):
    lines = generate_triangle_lines(height)
    for line in lines:
        print(line)
    return lines

if __name__ == '__main__':
    sample_height = 5
    result = print_triangle(sample_height)
    print(result)