def safe_get_first(data_list):
    if not data_list:
        raise IndexError("Cannot retrieve the first item from an empty list")
    return data_list[0]
if __name__ == '__main__':
    list1 = [10, 20, 30]
    list2 = []
    try:
        result1 = safe_get_first(list1)
        print(f"Result from list1: {result1}")
    except IndexError as e:
        print(f"Error for list1: {e}")
    try:
        result2 = safe_get_first(list2)
        print(f"Result from list2: {result2}")
    except IndexError as e:
        print(f"Error for list2: {e}")