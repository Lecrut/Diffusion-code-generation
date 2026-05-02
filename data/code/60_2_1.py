def get_last_item(data_list):
    if not data_list:
        raise IndexError("Cannot get the last item from an empty list")
    return data_list[-1]
if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = []
    try:
        last_item1 = get_last_item(list1)
        print(f"Last item of {list1}: {last_item1}")
    except IndexError as e:
        print(f"Error for list1: {e}")
    try:
        last_item2 = get_last_item(list2)
        print(f"Last item of {list2}: {last_item2}")
    except IndexError as e:
        print(f"Error for list2: {e}")