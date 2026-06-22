def fibonacci_generator(count):
    a = 0
    b = 1
    for _ in range(count):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    result = list(fibonacci_generator(1000))
    print(result)