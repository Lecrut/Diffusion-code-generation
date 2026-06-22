import random

def get_random_element(data_list):
    if not data_list:
        raise ValueError("List cannot be empty")
    return random.choice(data_list)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_random_element(sample_list)
    print(result)