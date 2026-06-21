def validate_data(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be a dictionary")
    for key, value in data.items():
        if not isinstance(key, int) or not isinstance(value, str):
            raise ValueError("Dictionary keys must be integers and values must be strings")

def map_dictionary_to_values(data):
    validate_data(data)
    return [value for value in data.values()]

if __name__ == '__main__':
    sample_data = {
        1: "apple",
        2: "zebra",
        3: "banana",
        4: "cat",
        5: "dog"
    }
    result = map_dictionary_to_values(sample_data)
    print(result)