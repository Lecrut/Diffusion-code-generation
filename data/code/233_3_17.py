WIDTH = 5
HEIGHT = 3
DIGITS = '0123456789'

def generate_rectangle_pattern(width=WIDTH, height=HEIGHT):
    return '\n'.join(DIGITS[i % len(DIGITS)] * width for i in range(height))

if __name__ == '__main__':
    print(generate_rectangle_pattern())