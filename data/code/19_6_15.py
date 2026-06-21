import random

def random_element_from_set(s):
    return random.choice(list(s))

if __name__ == '__main__':
    sample_set = {10, 20, 30, 40, 50}
    result = random_element_from_set(sample_set)
    print(result)