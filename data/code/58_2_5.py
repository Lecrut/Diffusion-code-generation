def get_first_item(lst):
    if not lst:
        raise ValueError("The list is empty")
    return lst[0]

if __name__ == '__main__':
    sample_list = [1, 2, 3]
    try:
        print(get_first_item(sample_list))
    except ValueError as e:
        print(e)

    empty_list = []
    try:
        print(get_first_item(empty_list))
    except ValueError as e:
        print(e)