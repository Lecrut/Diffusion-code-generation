def get_last_item(data_list):
    if not data_list:
        raise IndexError("Cannot get the last item from an empty list")
    return data_list[-1]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    try:
        last_fruit = get_last_item(sample_list)
        print(f"Last fruit in the list: {last_fruit}")
    except IndexError as e:
        print(e)

    empty_list = []
    try:
        last_item = get_last_item(empty_list)
        print(f"Last item in the empty list: {last_item}")
    except IndexError as e:
        print(e)