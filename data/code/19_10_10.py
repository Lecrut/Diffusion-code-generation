import random

def get_random_element(input_list):
    length = len(input_list)
    if length == 0:
        raise IndexError("Cannot choose from empty list")
    index = random.randrange(length)
    return input_list[index]

if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    selected = get_random_element(test_list)
    print(selected)