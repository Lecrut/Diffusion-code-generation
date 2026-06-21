from functools import reduce

def find_max(sequence):
    return reduce(lambda x, y: x if x > y else y, sequence)

if __name__ == '__main__':
    sample_sequence = [3, 5, 1, 2, 4]
    print(find_max(sample_sequence))