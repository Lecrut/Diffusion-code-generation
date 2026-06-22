def repeat_and_merge(dictionary, repetitions):
    if not isinstance(dictionary, dict) or not isinstance(repetitions, int) or repetitions < 0:
        raise ValueError("Invalid input: dictionary must be a dict and repetitions must be a non-negative integer")
    
    result = {}
    for key in dictionary:
        result[key] = [dictionary[key]] * repetitions
    return result

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2}
    repetitions = 3
    merged_dict = repeat_and_merge(sample_dict, repetitions)
    print(merged_dict)