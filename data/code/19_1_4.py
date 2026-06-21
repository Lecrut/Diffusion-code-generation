import random

def select_random_pair(d):
    if not d:
        raise ValueError("Dictionary is empty")
    key = random.choice(list(d.keys()))
    return key, d[key]

if __name__ == '__main__':
    sample_dict = {"apple": 3, "banana": 5, "cherry": 2}
    key, value = select_random_pair(sample_dict)
    print(key)
    print(value)