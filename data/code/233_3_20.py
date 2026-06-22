RECTANGLE_WIDTH = 5
RECTANGLE_HEIGHT = 3

def generate_rectangle_pattern(width=RECTANGLE_WIDTH, height=RECTANGLE_HEIGHT):
    pattern = ""
    digits = '0123456789'
    for y in range(height):
        row = digits[y % len(digits)] * width
        pattern += row + "\n"
    return pattern

if __name__ == '__main__':
    print(generate_rectangle_pattern())