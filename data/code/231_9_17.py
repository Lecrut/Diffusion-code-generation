def generate_pattern(length):
    pattern = 'abcde'
    repeated = (pattern * (length // 5 + 1))[:length]
    return repeated

if __name__ == '__main__':
    result = generate_pattern(50)
    print(result)