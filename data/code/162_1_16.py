def map_to_integers(data, mapping):
    result = {}
    for key, value in data.items():
        if key in mapping:
            result[key] = mapping.get(key)
        else:
            result[key] = 0
    return result

if __name__ == '__main__':
    sample_data = {
        "age": 25,
        "height": 180,
        "weight": None,
        "gender": "Male"
    }
    mapping = {
        "age": 1,
        "height": 2,
        "weight": 3,
        "gender": 4
    }
    integer_values = map_to_integers(sample_data, mapping)
    print(integer_values)