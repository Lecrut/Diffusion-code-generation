def get_first_item_safe(data_list):
    if not data_list:
        raise IndexError("Cannot retrieve the first item from an empty list")
    return data_list[0]
if __name__ == '__main__':
    list1 = [10, 20, 30]
    list2 = []
    try:
        item1 = get_first_item_safe(list1)
        print(f"First item from list1: {item1}")
    except IndexError as e:
        print(f"Error processing list1: {e}")
    try:
        item2 = get_first_item_safe(list2)
        print(f"First item from list2: {item2}")
    except IndexError as e:
        print(f"Error processing list2: {e}")