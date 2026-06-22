import itertools

def generate_sequence(length):
    return list(itertools.islice(itertools.cycle([1, 2, 3]), length))

if __name__ == '__main__':
    print(generate_sequence(15))