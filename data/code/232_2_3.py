import itertools

def generate_sequence(start=1, count=20):
    return list(itertools.islice(itertools.count(start), count))

if __name__ == '__main__':
    sequence = generate_sequence()
    for number in sequence:
        print(number)