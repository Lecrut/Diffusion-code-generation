import random

def get_random_value(data):
    if not data:
        return None
    keys = list(data.keys())
    selected_key = random.choice(keys)
    return data[selected_key]

if __name__ == '__main__':
    sample_dict = {'apple': 5, 'banana': 3, 'cherry': 7, 'date': 2}
    result = get_random_value(sample_dict)
    print(result)
    empty_dict = {}
    empty_result = get_random_value(empty_dict)
    print(empty_result)