HOLLOW_SQUARE_LINE_SIZE = 5

def generate_hollow_square_line_pattern(size=HOLLOW_SQUARE_LINE_SIZE):
    pattern = ""
    for i in range(size):
        if i == 0 or i == size - 1:
            pattern += "*" * size + "\n"
        else:
            pattern += "*" + " " * (size - 2) + "*\n"
    return pattern

if __name__ == '__main__':
    print(generate_hollow_square_line_pattern())