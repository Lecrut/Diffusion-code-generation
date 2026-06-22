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
    fib_numbers = get_first_n_fibonacci(count)
    print(fib_numbers[-1])
    print(fib_numbers[0])
    print(fib_numbers[10])
    print(fib_numbers[50])