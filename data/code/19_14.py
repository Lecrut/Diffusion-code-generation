import random

def get_random_value(data):
    if not data:
        return None
    keys = list(data.keys())
    selected_key = random.choice(keys)
    return data[selected_key]

if __name__ == '__main__':
    sample_dict = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}
    empty_dict = {}
    result1 = get_random_value(sample_dict)
    result2 = get_random_value(empty_dict)
    print(result1)
    print(result2)