def repeat_elements(input_set, times):
    if not isinstance(input_set, set) or not all(isinstance(item, int) for item in input_set):
        raise ValueError("Input must be a set of integers")
    if not isinstance(times, int) or times < 1:
        raise ValueError("Times must be a positive integer")

    return {item * times for item in input_set}

if __name__ == '__main__':
    sample_set = {1, 2, 3}
    sample_times = 3
    repeated_set = repeat_elements(sample_set, sample_times)
    print(repeated_set)