def fibonacci_generator(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    fib_list = list(fibonacci_generator(1000))
    print(fib_list[0])
    print(fib_list[1])
    print(fib_list[10])
    print(fib_list[100])
    print(fib_list[999])