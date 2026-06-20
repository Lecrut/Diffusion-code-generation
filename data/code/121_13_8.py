def compare_dict_sums(dict1, dict2):
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())
    return dict1 if sum1 > sum2 else dict2

if __name__ == '__main__':
    sample_dict1 = {'apple': 5, 'banana': 3}
    sample_dict2 = {'cherry': 4, 'date': 6}
    result = compare_dict_sums(sample_dict1, sample_dict2)
    print(result)