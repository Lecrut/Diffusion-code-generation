def generate_hello_pattern(times):
    pattern = ['hello'] * times
    return ' '.join(pattern)

if __name__ == '__main__':
    result = generate_hello_pattern(10)
    print(result)