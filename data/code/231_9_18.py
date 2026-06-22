def generate_pattern():
    pattern = 'abcde'
    repeated_pattern = pattern * 10
    return repeated_pattern[:50]

if __name__ == '__main__':
    print(generate_pattern())