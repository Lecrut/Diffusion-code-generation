def validate_max_value(max_value):
    if not isinstance(max_value, int) or max_value < 1:
        raise ValueError("Max value must be a positive integer")

def generate_triangle_pattern(max_value=5):
    validate_max_value(max_value)
    pattern = []
    for i in range(1, max_value + 1):
        spaces = ' ' * (max_value - i)
        numbers = ''.join(str(j) for j in range(1, i + 1))
        pattern.append(spaces + numbers)
    return '\n'.join(pattern)

if __name__ == '__main__':
    triangle_pattern = generate_triangle_pattern()
    print(triangle_pattern)