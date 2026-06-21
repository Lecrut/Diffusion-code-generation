import random

def get_random_element(input_set):
    if not input_set:
        raise ValueError("The input set cannot be empty")
    element_list = list(input_set)
    return random.choice(element_list)

if __name__ == '__main__':
    sample_set = {"apple", "banana", "cherry", "date", "elderberry"}
    result = get_random_element(sample_set)
    print(result)