def validate_list(lst):
    if not lst:
        raise ValueError("The input list is empty")

def get_first_element(lst):
    validate_list(lst)
    return lst[0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        print(get_first_element(sample_list))
    except ValueError as e:
        print(e)

    empty_list = []
    try:
        print(get_first_element(empty_list))
    except ValueError as e:
        print(e)

    single_element_list = [42]
    try:
        print(get_first_element(single_element_list))
    except ValueError as e:
        print(e)