def find_largest_value(data_dict):
    if not data_dict:
        raise ValueError("Input dictionary cannot be empty")
    
    max_value = None
    for value in data_dict.values():
        if max_value is None or value > max_value:
            max_value = value
    
    return max_value

if __name__ == '__main__':
    sample_dict = {
        "key1": 10,
        "key2": 20,
        "key3": 30,
        "key4": 40,
        "key5": 50
    }
    
    print(f"Largest value in {sample_dict}: {find_largest_value(sample_dict)}")