def print_dict_pairs(data):
    for key, value in data.items():
        print(f"Key: {key}, Value: {value}")
if __name__ == '__main__':
    sample_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "occupation": "Engineer"
    }
    print_dict_pairs(sample_dict)