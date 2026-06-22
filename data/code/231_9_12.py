def generate_pattern(length):
    pattern = 'abcde'
    return (pattern * (length // len(pattern) + 1))[:length]

if __name__ == '__main__':
    result = generate_pattern(50)
    print(result)