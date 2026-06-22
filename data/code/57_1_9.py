def generate_fibonacci(count):
    if count <= 0:
        return
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    first_fifty = list(generate_fibonacci(50))
    for number in first_fifty:
        print(number)