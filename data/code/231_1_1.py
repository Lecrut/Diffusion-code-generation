import itertools

def repeating_sequence():
    return list(itertools.islice(itertools.cycle([1, 2, 3]), 15))

if __name__ == '__main__':
    print(repeating_sequence())