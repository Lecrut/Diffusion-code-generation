def growing_sequence(limit):
    return (x for x in range(1, limit + 1))

if __name__ == '__main__':
    max_limit = 50
    sequence_generator = growing_sequence(max_limit)
    for number in sequence_generator:
        print(number)