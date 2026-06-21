import random

def get_random_element(data):
    if not data:
        return None
    index = random.randint(0, len(data) - 1)
    return data[index]

if __name__ == '__main__':
    sample_list = [10, 25, 30, 45, 55, 60, 75, 80, 90, 100]
    result = get_random_element(sample_list)
    print(result)