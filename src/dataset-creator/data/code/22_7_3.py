def find_matching_items(dict1, dict2):
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
        'd': 40
    }
    matching_generator = find_matching_items(data1, data2)
    results = list(matching_generator)
    for key, val1, val2 in results:
        print(f"Key: {key}, Value1: {val1}, Value2: {val2}")