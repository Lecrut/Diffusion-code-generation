import random

def select_random_pair(data):
    if not data:
        return None, None
    key = random.choice(list(data.keys()))
    value = data[key]
    return key, value

if __name__ == '__main__':
    sample_dict = {
        'apple': 1,
        'banana': 2,
        'cherry': 3,
        'date': 4,
        'elderberry': 5
    }
    selected_key, selected_value = select_random_pair(sample_dict)
    print(f"Key: {selected_key}, Value: {selected_value}")