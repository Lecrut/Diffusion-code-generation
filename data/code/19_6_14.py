import random

def get_random_element(input_set):
    if not input_set:
        return None
    list_items = list(input_set)
    return random.choice(list_items)

if __name__ == '__main__':
    sample_set = {'apple', 'banana', 'cherry', 'date', 'elderberry'}
    result = get_random_element(sample_set)
    print(result)