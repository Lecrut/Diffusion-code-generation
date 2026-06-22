def generate_rectangle_pattern(width, height):
    if not (isinstance(width, int) and isinstance(height, int)):
        raise ValueError("Width and height must be integers.")
    
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be greater than zero.")
    
    digits = '0123456789'
    pattern = '\n'.join(digits[i % len(digits)] * width for i in range(height))
    return pattern

if __name__ == '__main__':
    print(generate_rectangle_pattern(5, 3))