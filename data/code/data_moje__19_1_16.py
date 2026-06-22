import random

def get_random_pair(data_dict):
    if not data_dict:
        raise ValueError("Dictionary cannot be empty")
    key = random.choice(list(data_dict.keys()))
    value = data_dict[key]
    return key, value

if __name__ == '__main__':
    sample_data = {"apple": 5, "banana": 3, "cherry": 7, "date": 2}
    result_key, result_value = get_random_pair(sample_data)
    print(result_key)
    print(result_value)