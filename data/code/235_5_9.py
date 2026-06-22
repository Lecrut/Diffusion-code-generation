def validate_input(max_value):
    if not isinstance(max_value, int) or max_value < 1:
        raise ValueError("max_value must be a positive integer")

def generate_hypotenuse_pattern(max_value):
    validate_input(max_value)
    pattern = []
    for i in range(1, max_value + 1):
        spaces = ' ' * (max_value - i)
        numbers = ''.join(str(j) for j in range(1, i + 1))
        pattern.append(spaces + numbers)
    return '\n'.join(pattern)

if __name__ == '__main__':
    print(generate_hypotenuse_pattern(5))