if __name__ == '__main__':
    input_dict = {
        "Alice": 1,
        "Bob": 2,
        "Charlie": 3,
        "David": 4
    }
    value_map = {name: value for name, value in input_dict.items()}
    print(value_map)