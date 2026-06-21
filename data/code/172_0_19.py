def map_dict_to_list(data):
    return list(data.values())

if __name__ == '__main__':
    sample_data = {
        "red": "apple",
        "green": "banana",
        "yellow": "cherry",
        "blue": "grape"
    }
    mapped_list = map_dict_to_list(sample_data)
    print(mapped_list)