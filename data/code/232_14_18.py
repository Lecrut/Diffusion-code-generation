def square_sequence(n):
    for i in range(1, n + 1):
        yield i * i

if __name__ == '__main__':
    sequence = square_sequence(5)
    result = [next(sequence) for _ in range(5)]
    print(result)