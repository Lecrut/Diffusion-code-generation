WIDTH = 5

def generate_arrowhead_pattern():
    pattern = ""
    for i in range(1, WIDTH + 1):
        pattern += " " * (WIDTH - i) + "*" * (2 * i - 1) + "\n"
    return pattern

if __name__ == '__main__':
    print(generate_arrowhead_pattern())