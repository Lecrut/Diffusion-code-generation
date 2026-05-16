def map_to_simple_values(input_dict):
    return {key: value for key, value in input_dict.items()}
if __name__ == '__main__':
    sample_dict = {
        "name": "Alice",
        "age": "30",
        "city": "New York",
        "occupation": "Engineer"
    }
    result_dict = map_to_simple_values(sample_dict)
    print(result_dict)