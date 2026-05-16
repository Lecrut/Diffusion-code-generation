def sum_three_iterative(a, b, c):
    total = 0
    yield a
    total += a
    yield b
    total += b
    yield c
    total += c
    yield total
if __name__ == '__main__':
    num1, num2, num3 = 10, 20, 30
    generator = sum_three_iterative(num1, num2, num3)
    result = sum(generator)
    print(result)