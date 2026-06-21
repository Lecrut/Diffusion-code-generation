import random

def get_random_element(data_set):
    if not data_set:
        return None
    elements_list = list(data_set)
    return random.choice(elements_list)

if __name__ == '__main__':
    sample_set = {'apple', 'banana', 'cherry', 'date'}
    result = get_random_element(sample_set)
    print(result)
    empty_set = set()
    empty_result = get_random_element(empty_set)
    print(empty_result)