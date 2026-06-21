def convert_to_dict(store_list):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in store_list):
        raise ValueError("All elements must be tuples of length 2")
    
    return dict(store_list)

if __name__ == '__main__':
    sample_data = [
        ("StoreA", 30),
        ("StoreB", 25),
        ("StoreC", 35),
        ("StoreD", 28)
    ]
    try:
        result_dict = convert_to_dict(sample_data)
        print(result_dict)
    except ValueError as e:
        print(e)