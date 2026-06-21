def validate_input(iterable):
    if not isinstance(iterable, (list, tuple)):
        raise ValueError("Input must be a list or tuple")

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
    sample_list_2 = ['a', 'b', 'c']
    sample_tuple = (10, 20, 30)
    
    validate_input(sample_list_1)
    print(f"Frequency for {sample_list_1}: {calculate_frequency(sample_list_1)}")
    
    validate_input(sample_list_2)
    print(f"Frequency for {sample_list_2}: {calculate_frequency(sample_list_2)}")
    
    validate_input(sample_tuple)
    print(f"Frequency for {sample_tuple}: {calculate_frequency(sample_tuple)}")