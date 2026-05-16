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
    result_generator = sum_three_iterative(10, 20, 30)
    print(list(result_generator))