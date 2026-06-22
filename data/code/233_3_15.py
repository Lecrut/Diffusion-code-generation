def generate_rectangle_pattern(width, height):
    digits = '0123456789'
    pattern = '\n'.join(digits[i % len(digits)] * width for i in range(height))
    return pattern

if __name__ == '__main__':
    sample_width = 6
    sample_height = 4
    print(generate_rectangle_pattern(sample_width, sample_height))