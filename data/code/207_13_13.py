from functools import reduce

def find_max_sequence(sequence):
    if not sequence:
        raise ValueError("Sequence cannot be empty")
    
    max_value = reduce(lambda x, y: x if x > y else y, sequence)
    return max_value

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Sample data:", sample_data)
    try:
        print("Max value:", find_max_sequence(sample_data))
    except ValueError as e:
        print(e)

    sample_data_2 = [10, 5, 20, 3, 15]
    print("\nSample data:", sample_data_2)
    try:
        print("Max value:", find_max_sequence(sample_data_2))
    except ValueError as e:
        print(e)