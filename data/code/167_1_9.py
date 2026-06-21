def convert_to_dict(tuples_list):
    return dict(tuples_list)

if __name__ == '__main__':
    sample_data = [
        ("StoreA", 30),
        ("StoreB", 25),
        ("StoreC", 35),
        ("StoreD", 28)
    ]
    result_dict = convert_to_dict(sample_data)
    print(result_dict)