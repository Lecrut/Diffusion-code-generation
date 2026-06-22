def generate_rectangle_pattern(width, height):
    digits = '0123456789'
    pattern = '\n'.join(digits * (width // len(digits)) + digits[:width % len(digits)] for _ in range(height))
    return pattern

if __name__ == '__main__':
    print(generate_rectangle_pattern(10, 5))