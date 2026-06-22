PATTERN = 'hello'

def generate_pattern():
    return ' '.join([PATTERN] * 10)

if __name__ == '__main__':
    result = generate_pattern()
    print(result)