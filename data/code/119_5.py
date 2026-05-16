def reverse_yield(a, b):
    yield b
    yield a
if __name__ == '__main__':
    num1 = 10
    num2 = 20
    for item in reverse_yield(num1, num2):
        print(item)