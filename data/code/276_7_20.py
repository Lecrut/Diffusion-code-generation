def repeat_elements(input_set, times):
    repeated_set = set(item * times for item in input_set)
    return repeated_set

if __name__ == '__main__':
    sample_set = {1, 2, 3}
    sample_times = 3
    result = repeat_elements(sample_set, sample_times)
    print(result)