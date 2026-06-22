def fibonacci_generator():
    a, b = 0, 1
    for _ in range(1000):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    fibs = list(fibonacci_generator())
    print(fibs[:10])
    print(fibs[999])