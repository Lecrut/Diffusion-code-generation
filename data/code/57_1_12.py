def generate_fibonacci(count):
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    result = list(generate_fibonacci(1000))
    print(result[0])
    print(result[1])
    print(result[999])