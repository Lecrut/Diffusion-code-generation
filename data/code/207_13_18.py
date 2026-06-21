from functools import reduce

def find_max_value(sequence):
    return reduce(lambda a, b: a if a > b else b, sequence)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Maximum value:", find_max_value(sample_data))