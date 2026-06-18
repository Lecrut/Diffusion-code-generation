def find_matching_tuples(dict1, dict2):
    for key, value1 in dict1.items():
        if key in dict2:
            value2 = dict2[key]
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
        'b': 200,
        'c': 300,
        'e': 500,
        'f': 600
    }
    matching_generator = find_matching_tuples(data1, data2)
    results = list(matching_generator)
    print(results)