def access_first_element(data):
    return data[0]

if __name__ == '__main__':
    sample_data = {
        'integers': [10, 20, 30],
        'strings': ["apple", "banana", "cherry"],
        'floats': [3.14, 2.71, 1.618],
        'booleans': [True, False, True]
    }

    for category, data_list in sample_data.items():
        first_element = access_first_element(data_list)
        print(f"First element of {category} list: {first_element}")