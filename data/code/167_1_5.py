def convert_to_dict(store_list):
    return dict(store_list)

if __name__ == '__main__':
    sample_data = [
        ("StoreA", 30),
        ("StoreB", 25),
        ("StoreC", 35),
        ("StoreD", 28)
    ]
    result = convert_to_dict(sample_data)
    print(result)