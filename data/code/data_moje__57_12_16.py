def generate_fibonacci(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

if __name__ == '__main__':
    result = generate_fibonacci(20)
    print(result)