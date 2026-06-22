def square_sequence(n):
    for i in range(1, n + 1):
        yield i * i

if __name__ == '__main__':
    iterations = 5
    result = list(square_sequence(iterations))
    print(result)