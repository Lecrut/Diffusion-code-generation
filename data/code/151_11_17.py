def validate_input(list_a, list_b):
    if not isinstance(list_a, list) or not isinstance(list_b, list):
        raise ValueError("Both inputs must be lists")

def combine_lists_extend(list_a, list_b):
    validate_input(list_a, list_b)
    list_a.extend(list_b)

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combine_lists_extend(list1, list2)
    print(list1)