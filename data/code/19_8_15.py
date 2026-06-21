import random

def get_random_value(value_range, data_list):
    if not data_list:
        return None
    index = random.randint(0, len(data_list) - 1)
    return data_list[index]

if __name__ == '__main__':
    sample_range = range(10, 20)
    sample_list = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    result = get_random_value(sample_range, sample_list)
    print(result)