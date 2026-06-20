MAX_FIB_LIMIT = 100

def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    for num in fibonacci_generator(MAX_FIB_LIMIT):
        print(num)