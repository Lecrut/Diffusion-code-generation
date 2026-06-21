from functools import reduce

def find_max_value(data_sequence):
    if not data_sequence:
        raise ValueError("Input sequence cannot be empty")
    
    return reduce(lambda x, y: x if x > y else y, data_sequence)

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Maximum value in sequence:", find_max_value(sample_data))