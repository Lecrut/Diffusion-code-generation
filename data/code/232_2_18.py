import itertools

def generate_sequence():
    return list(itertools.islice(itertools.count(1), 20))

if __name__ == '__main__':
    sample_sequence = generate_sequence()
    for number in sample_sequence:
        print(number)