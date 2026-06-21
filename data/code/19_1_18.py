import random

def select_random_pair(data):
    if not data:
        raise ValueError("Dictionary cannot be empty")
    key = random.choice(list(data.keys()))
    return key, data[key]

if __name__ == '__main__':
    sample_dict = {'apple': 5, 'banana': 3, 'cherry': 8, 'date': 2}
    result = select_random_pair(sample_dict)
    print(result)