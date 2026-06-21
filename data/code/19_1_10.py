import random

def select_random_pair(data):
    if not data:
        raise ValueError("Dictionary cannot be empty")
    key = random.choice(list(data.keys()))
    return key, data[key]

if __name__ == '__main__':
    sample_data = {"apple": 1, "banana": 2, "cherry": 3, "date": 4}
    selected_key, selected_value = select_random_pair(sample_data)
    print(selected_key, selected_value)