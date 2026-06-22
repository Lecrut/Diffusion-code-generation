def fibonacci_generator(count):
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    gen = fibonacci_generator(1000)
    for i in range(10):
        print(gen.__next__())
    results = []
    for _ in range(1000):
        results.append(gen.__next__())
    print(results[-1])
    print(results[-2])