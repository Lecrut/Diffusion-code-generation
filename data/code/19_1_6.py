import random

def select_random_key_value(data):
    if not data:
        raise ValueError("Dictionary cannot be empty")
    key = random.choice(list(data.keys()))
    return key, data[key]

if __name__ == '__main__':
    sample_dict = {'apple': 3, 'banana': 5, 'cherry': 8, 'date': 2}
    result_key, result_value = select_random_key_value(sample_dict)
    print(f"Key: {result_key}, Value: {result_value}")