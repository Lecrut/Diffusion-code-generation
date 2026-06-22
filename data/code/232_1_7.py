def growing_sequence(limit):
    return (i for i in range(1, limit + 1))

if __name__ == '__main__':
    for number in growing_sequence(10):
        print(number)