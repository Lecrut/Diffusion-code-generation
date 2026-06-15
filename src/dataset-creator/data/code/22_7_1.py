def find_matching_tuples(dict1, dict2):
    for key, value1 in dict1.items():
        if key in dict2:
            value2 = dict2[key]
            if value1 == value2:
                yield (key, value1, value2)
if __name__ == '__main__':
    data1 = {
        'a': 10,
        'b': 20,
        'c': 30,
        'd': 40,
        'e': 50
    }
    data2 = {
        'a': 10,
        'b': 25,
        'c': 30,
        'f': 60,
        'e': 50
    }
    matching_tuples = find_matching_tuples(data1, data2)
    results = list(matching_tuples)
    print(results)