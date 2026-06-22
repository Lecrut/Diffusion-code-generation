import itertools

def create_repeating_sequence(length):
    return list(itertools.islice(itertools.cycle([1, 2, 3]), length))

if __name__ == '__main__':
    print(create_repeating_sequence(15))