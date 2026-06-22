def growing_sequence(limit):
    return (x for x in range(1, limit + 1))

if __name__ == '__main__':
    sequence = growing_sequence(50)
    for number in sequence:
        print(number)