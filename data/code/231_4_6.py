def generate_pattern(length):
    return [i % 2 for i in range(length)]

if __name__ == '__main__':
    pattern = generate_pattern(50)
    print(pattern)