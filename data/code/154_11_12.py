def validate_input(iterable):
    if not isinstance(iterable, (list, tuple, set)):
        raise ValueError("Input must be a list, tuple, or set")

def calculate_frequency(iterable):
    frequency = {}
    for item in iterable:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    validate_input(sample_list_1)
    print(f"Frequency for {sample_list_1}: {calculate_frequency(sample_list_1)}")

    sample_list_2 = ['a', 'b', 'c']
    validate_input(sample_list_2)
    print(f"Frequency for {sample_list_2}: {calculate_frequency(sample_list_2)}")

    sample_tuple = (10, 20, 30)
    validate_input(sample_tuple)
    print(f"Frequency for {sample_tuple}: {calculate_frequency(sample_tuple)}")

    sample_empty = []
    validate_input(sample_empty)
    print(f"Frequency for {sample_empty}: {calculate_frequency(sample_empty)}")