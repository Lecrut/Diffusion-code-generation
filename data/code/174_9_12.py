def dict_intersection(dict1, dict2):
    intersection = {}
    for key in dict1:
        if key in dict2:
            intersection[key] = dict1[key]
    return intersection
if __name__ == '__main__':
    sample_dict1 = {'apple': 1, 'banana': 2, 'cherry': 3}
    sample_dict2 = {'banana': 4, 'cherry': 5, 'date': 6}
    result = dict_intersection(sample_dict1, sample_dict2)
    print(result)