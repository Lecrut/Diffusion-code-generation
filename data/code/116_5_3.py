def sum_three_iterative(a, b, c):
    current_sum = 0
    yield a
    current_sum += a
    yield b
    current_sum += b
    yield c
    current_sum += c
    yield current_sum
if __name__ == '__main__':
    gen = sum_three_iterative(10, 20, 30)
    results = list(gen)
    print(results)