def fibonacci_generator():
    a, b = 0, 1
    for _ in range(10):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    result = list(fibonacci_generator())
    print(result)