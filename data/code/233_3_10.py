def generate_rectangle(width, height):
    digits = '0123456789'
    pattern = ''.join(digits[i % len(digits)] for i in range(width * height))
    return '\n'.join(pattern[i:i+width] for i in range(0, width * height, width))

if __name__ == '__main__':
    print(generate_rectangle(10, 5))