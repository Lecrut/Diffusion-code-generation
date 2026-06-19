def validate_lists(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists.")
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")

def absolute_difference_generator(list1, list2):
    validate_lists(list1, list2)
    for num1, num2 in zip(list1, list2):
        yield abs(num1 - num2)

if __name__ == '__main__':
    try:
        list_a = [8, 16, 24, 32]
        list_b = [4, 8, 12, 16]
        for difference in absolute_difference_generator(list_a, list_b):
            print(difference)
    except (TypeError, ValueError) as e:
        print(e)