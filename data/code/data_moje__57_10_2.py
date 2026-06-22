def fibonacci_generator():
    a, b = 0, 1
    count = 0
    while count < 10:
        yield a
        a, b = b, a + b
        count += 1

if __name__ == '__main__':
    for number in fibonacci_generator():
        print(number)