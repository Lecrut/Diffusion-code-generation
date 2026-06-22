def find_min_max_values(data_dict):
    min_key = min(data_dict, key=data_dict.get)
    max_key = max(data_dict, key=data_dict.get)
    return (min_key, data_dict[min_key]), (max_key, data_dict[max_key])

if __name__ == '__main__':
    sample_data = {
        'apple': 50,
        'banana': 30,
        'cherry': 70,
        'date': 40
    }
    min_value, max_value = find_min_max_values(sample_data)
    print(f"Min: {min_value}, Max: {max_value}")