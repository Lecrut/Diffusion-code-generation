from functools import reduce

def find_largest_item(sequence):
    return reduce(lambda x, y: x if x > y else y, sequence)

if __name__ == '__main__':
    sample_sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_largest_item(sample_sequence))