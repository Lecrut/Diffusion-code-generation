def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def get_first_n_fibonacci(n):
    gen = fibonacci_generator()
    result = []
    for _ in range(n):
        result.append(next(gen))
    return result

if __name__ == '__main__':
    count = 1000
    first_thousand = get_first_n_fibonacci(count)
    print(first_thousand)