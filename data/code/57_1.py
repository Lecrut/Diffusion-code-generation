def fibonacci_generator(count=1000):
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    results = list(fibonacci_generator(1000))
    print(results[0])
    print(results[1])
    print(results[999])
    print(len(results))