def get_keys(input_dict):
    return list(input_dict.keys())
if __name__ == '__main__':
    sample_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "occupation": "Engineer"
    }
    result_list = get_keys(sample_dict)
    print(result_list)