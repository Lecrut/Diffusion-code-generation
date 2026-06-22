DIGITS = '0123456789'
WIDTH = 5
HEIGHT = 3

def generate_rectangle_pattern(width, height):
    pattern = ""
    for y in range(height):
        for x in range(width):
            digit_index = (x + y) % len(DIGITS)
            pattern += DIGITS[digit_index]
        pattern += "\n"
    return pattern

if __name__ == '__main__':
    print(generate_rectangle_pattern(WIDTH, HEIGHT))