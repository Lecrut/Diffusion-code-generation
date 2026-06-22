def generate_rectangle_pattern(width, height):
    digits = '0123456789'
    rows = [digits[i % len(digits): i % len(digits) + width] for i in range(height * width)]
    pattern = '\n'.join(rows)
    return pattern

if __name__ == '__main__':
    print(generate_rectangle_pattern(5, 3))