def convert_to_dict(data):
    return {name: age for name, age in data}
if __name__ == '__main__':
    sample_data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    result_dict = convert_to_dict(sample_data)
    print(result_dict)