import random

def get_random_element(items):
    length = len(items)
    if length == 0:
        raise ValueError("Cannot select from empty list")
    index = random.randint(0, length - 1)
    selected_item = items[index]
    return selected_item

if __name__ == '__main__':
    test_numbers = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
    output_value = get_random_element(test_numbers)
    print(output_value)