if __name__ == '__main__':
    HELLO_WORLD = 'Hello World'
    REPEAT_COUNT = 100

    result = '\n'.join([HELLO_WORLD for _ in range(REPEAT_COUNT)])
    print(result)