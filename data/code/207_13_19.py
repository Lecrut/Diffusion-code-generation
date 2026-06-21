from functools import reduce

def find_max_value(sequence):
    if not sequence:
        raise ValueError("Sequence is empty")
    return reduce(lambda x, y: x if x > y else y, sequence)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    try:
        print("Maximum value:", find_max_value(sample_data))
    except ValueError as e:
        print(e)