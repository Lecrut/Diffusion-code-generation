import random

def get_random_index_value(index_range, value_list):
    if not value_list:
        raise ValueError("Value list cannot be empty")
    if len(value_list) != index_range.stop - index_range.start:
        raise ValueError("Index range length must match value list length")
    random_index = random.randrange(index_range.start, index_range.stop, index_range.step)
    return value_list[random_index]

if __name__ == '__main__':
    sample_range = range(10)
    sample_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    result = get_random_index_value(sample_range, sample_list)
    print(result)