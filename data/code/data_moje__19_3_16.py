import random

SAMPLE_VALUES = (10, 20, 30, 40, 50)
EMPTY_VALUE = ()

def retrieve_random_element(source_tuple):
    if len(source_tuple) == 0:
        return None
    index = random.randint(0, len(source_tuple) - 1)
    return source_tuple[index]

if __name__ == '__main__':
    first_result = retrieve_random_element(SAMPLE_VALUES)
    second_result = retrieve_random_element(EMPTY_VALUE)
    print(first_result)
    print(second_result)