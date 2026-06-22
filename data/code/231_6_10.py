def create_hello_pattern():
    hello = "hello "
    pattern = hello * 10
    return pattern.strip()

if __name__ == '__main__':
    result = create_hello_pattern()
    print(result)