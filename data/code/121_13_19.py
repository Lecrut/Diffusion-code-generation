def compare_dict_sums(dict1, dict2):
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())
    return dict1 if sum1 > sum2 else dict2

if __name__ == '__main__':
    sample_dict1 = {'x': 30, 'y': 40}
    sample_dict2 = {'m': 50, 'n': 60, 'o': 70}
    result = compare_dict_sums(sample_dict1, sample_dict2)
    print(result)