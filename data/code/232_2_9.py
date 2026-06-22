import itertools

def generate_sequence(start=1, count=20):
    return list(itertools.islice(itertools.count(start), count))

if __name__ == '__main__':
    sample_count = 20
    start_number = 1
    sequence = generate_sequence(start_number, sample_count)
    for number in sequence:
        print(number)