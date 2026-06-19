def get_last_item(mutable_list):
    if not mutable_list:
        raise ValueError("The list is empty")
    return mutable_list[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        print(get_last_item(sample_list))
    except ValueError as e:
        print(e)

    empty_list = []
    try:
        print(get_last_item(empty_list))
    except ValueError as e:
        print(e)