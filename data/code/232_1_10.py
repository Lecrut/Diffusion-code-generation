def growing_sequence(limit):
    return (x for x in range(1, limit + 1))

if __name__ == '__main__':
    seq = growing_sequence(10)
    for num in seq:
        print(num)