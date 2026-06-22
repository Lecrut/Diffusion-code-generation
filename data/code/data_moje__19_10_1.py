import random

def get_random_element(int_list):
    return random.choice(int_list)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    result = get_random_element(sample_data)
    print(result)