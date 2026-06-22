import random

def select_random_pair(data):
    if not data:
        raise ValueError("Dictionary cannot be empty")
    key = random.choice(list(data.keys()))
    return key, data[key]

if __name__ == '__main__':
    sample_dict = {'apple': 5, 'banana': 3, 'cherry': 7, 'date': 2}
    selected_key, selected_value = select_random_pair(sample_dict)
    print(f"Key: {selected_key}, Value: {selected_value}")