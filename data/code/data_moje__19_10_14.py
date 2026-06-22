import random

def get_random_element(input_list):
    index = random.randrange(len(input_list))
    selected_value = input_list[index]
    return selected_value

if __name__ == '__main__':
    test_numbers = [7, 14, 21, 28, 35, 42, 49]
    output = get_random_element(test_numbers)
    print(output)