def generate_fibonacci(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

if __name__ == '__main__':
    fib_numbers = list(generate_fibonacci(1000))
    print(fib_numbers[:10])
    print(len(fib_numbers))
    print(fib_numbers[-1])