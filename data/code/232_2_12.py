import itertools

def generate_sequence(count):
    return list(itertools.islice(itertools.count(start=1), count))

if __name__ == '__main__':
    sample_count = 20
    sequence = generate_sequence(sample_count)
    for number in sequence:
        print(number)