def get_last_item(data_list):
    if not data_list:
        raise IndexError("Cannot retrieve the last item from an empty list")
    return data_list[-1]

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20, 25]
    try:
        last_item = get_last_item(sample_list)
        print(f"The last item of {sample_list} is: {last_item}")
    except IndexError as e:
        print(f"Error: {e}")

    empty_list = []
    try:
        last_item_empty = get_last_item(empty_list)
        print(f"The last item of {empty_list} is: {last_item_empty}")
    except IndexError as e:
        print(f"Error: {e}")