def create_rectangle_pattern(width, height):
    digits = '0123456789'
    pattern = '\n'.join(digits[i % len(digits)] * width for i in range(height))
    return pattern

if __name__ == '__main__':
    print(create_rectangle_pattern(5, 3))