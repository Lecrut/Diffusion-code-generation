import random

def pick_random_from_set(input_set):
    converted_list = list(input_set)
    list_length = len(converted_list)
    if list_length == 0:
        return None
    random_index = random.randint(0, list_length - 1)
    selected_value = converted_list[random_index]
    return selected_value

if __name__ == '__main__':
    test_data = {'apple', 'banana', 'cherry', 'date'}
    output = pick_random_from_set(test_data)
    print(output)