def compare_dict_sums(dict1, dict2):
    if not all(isinstance(val, (int, float)) for val in dict1.values()):
        raise ValueError("All values in dict1 must be numeric")
    if not all(isinstance(val, (int, float)) for val in dict2.values()):
        raise ValueError("All values in dict2 must be numeric")

    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())

    return dict1 if sum1 > sum2 else dict2

if __name__ == '__main__':
    sample_dict1 = {'a': 10, 'b': 20}
    sample_dict2 = {'c': 30, 'd': 40}
    result = compare_dict_sums(sample_dict1, sample_dict2)
    print(result)