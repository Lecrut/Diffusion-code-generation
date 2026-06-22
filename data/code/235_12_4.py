CHAR_MAP = {'*': 'A'}

def generate_char_pattern(n):
    pattern = []
    for i in range(1, n + 1):
        line = CHAR_MAP['*'] * i
        pattern.append(line.center(n))
    return "\n".join(pattern)

if __name__ == '__main__':
    sample_number = 5
    pattern = generate_char_pattern(sample_number)
    print(pattern)