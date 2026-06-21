def convert_to_dict(tuples_list):
    if not isinstance(tuples_list, list) or not all(isinstance(item, tuple) and len(item) == 2 for item in tuples_list):
        raise ValueError("Input must be a list of tuples with two elements each.")
    
    return dict(tuples_list)

if __name__ == '__main__':
    sample_data = [
        ("StoreA", 30),
        ("StoreB", 25),
        ("StoreC", 35),
        ("StoreD", 28)
    ]
    result = convert_to_dict(sample_data)
    print(result)