def generate_pattern():
    pattern = 'abcde'
    repeated_pattern = (pattern * 10)[:50]
    return repeated_pattern

if __name__ == '__main__':
    print(generate_pattern())