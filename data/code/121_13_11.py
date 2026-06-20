def sum_of_dict_values(dictionary):
    return sum(dictionary.values())

def compare_dict_sums(dict1, dict2):
    if not all(isinstance(val, (int, float)) for val in dict1.values()):
        raise ValueError("Dictionary values must be numeric")
    if not all(isinstance(val, (int, float)) for val in dict2.values()):
        raise ValueError("Dictionary values must be numeric")

    sum1 = sum_of_dict_values(dict1)
    sum2 = sum_of_dict_values(dict2)

    return dict1 if sum1 > sum2 else dict2

if __name__ == '__main__':
    sample_dict1 = {'a': 10, 'b': 20}
    sample_dict2 = {'c': 30, 'd': 40}
    result = compare_dict_sums(sample_dict1, sample_dict2)
    print(result)