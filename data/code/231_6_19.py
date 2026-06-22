PATTERN = 'hello'
COUNT = 10

def generate_pattern():
    return (PATTERN + ' ') * COUNT.strip()

if __name__ == '__main__':
    result = generate_pattern()
    print(result)