THRESHOLD = 80

def filter_dictionary(input_dict):
    return {key: value for key, value in input_dict.items() if value >= THRESHOLD}

if __name__ == '__main__':
    sample_dict = {
        "Alice": 75,
        "Bob": 92,
        "Charlie": 88,
        "David": 70
    }
    filtered_dict = filter_dictionary(sample_dict)
    print(filtered_dict)