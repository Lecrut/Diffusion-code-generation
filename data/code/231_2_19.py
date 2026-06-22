PATTERN_SIZE = 10

def generate_pattern():
    pattern = []
    for i in range(PATTERN_SIZE):
        row = ['*'] * (i + 1) + ['.'] * (PATTERN_SIZE - i - 1)
        pattern.append(''.join(row))
    return pattern

if __name__ == '__main__':
    pattern = generate_pattern()
    for line in pattern:
        print(line)