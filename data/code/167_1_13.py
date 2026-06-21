def convert_to_dict(data):
    return dict(data)

if __name__ == '__main__':
    sample_data = [
        ("StoreA", 30),
        ("StoreB", 25),
        ("StoreC", 35),
        ("StoreD", 28)
    ]
    result = convert_to_dict(sample_data)
    print(result)