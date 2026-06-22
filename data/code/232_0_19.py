if __name__ == '__main__':
    count = 50
    if not isinstance(count, int) or count < 1:
        raise ValueError("Count must be a positive integer")

    sequence = [i for i in range(1, count + 1)]
    print(*sequence)