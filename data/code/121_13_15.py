def sum_of_values(dictionary):
    return sum(dictionary.values())

def compare_dict_sums(dict1, dict2):
    sum1 = sum_of_values(dict1)
    sum2 = sum_of_values(dict2)
    return dict1 if sum1 > sum2 else dict2

if __name__ == '__main__':
    sample_dict1 = {'a': 10, 'b': 20}
    sample_dict2 = {'c': 30, 'd': 40}
    result = compare_dict_sums(sample_dict1, sample_dict2)
    print(result)