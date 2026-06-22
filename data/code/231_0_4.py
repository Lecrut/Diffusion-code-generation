def generate_pattern():
    pattern = ''.join(['AB' for _ in range(10)])
    return pattern

if __name__ == '__main__':
    print(generate_pattern())