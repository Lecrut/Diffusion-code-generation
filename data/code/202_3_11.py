def find_highest_value(data_dict):
    return max(data_dict.values())

if __name__ == '__main__':
    sample_dict = {
        'a': 10,
        'b': 20,
        'c': 5,
        'd': 30
    }
    print(f"Highest value in {sample_dict}: {find_highest_value(sample_dict)}")