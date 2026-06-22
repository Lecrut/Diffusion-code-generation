CHARS = 'abcde'
REPEAT_COUNT = 10

def generate_pattern():
    return (CHARS * REPEAT_COUNT)[:50]

if __name__ == '__main__':
    result = generate_pattern()
    print(result)