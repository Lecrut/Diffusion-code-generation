def map_to_simple_values(data):
    return {key: value for key, value in data.items()}
if __name__ == '__main__':
    sample_dict = {
        "name": "Alice",
        "age": "30",
        "city": "New York",
        "occupation": "Engineer"
    }
    result_dict = map_to_simple_values(sample_dict)
    print(result_dict)