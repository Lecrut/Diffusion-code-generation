import random

def get_random_key_value(data):
    if not data:
        raise ValueError("Dictionary cannot be empty")
    key = random.choice(list(data.keys()))
    return key, data[key]

if __name__ == '__main__':
    sample_data = {'apple': 5, 'banana': 3, 'cherry': 8, 'date': 12}
    result_key, result_value = get_random_key_value(sample_data)
    print(f"{result_key}: {result_value}")