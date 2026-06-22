def generate_fibonacci(count):
    if count <= 0:
        return
    a, b = (0, 1)
    for _ in range(count):
        yield a
        a, b = (b, a + b)
if __name__ == '__main__':
    fib_sequence = list(generate_fibonacci(10))
    print(fib_sequence)
    tenth_fib = list(generate_fibonacci(10))[-1]
    print(tenth_fib)
    one_thousandth = list(generate_fibonacci(1000))[-1]
    print(one_thousandth)