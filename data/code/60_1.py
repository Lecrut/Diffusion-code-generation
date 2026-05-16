def get_last_item(data):
    if not data:
        raise IndexError("list is empty")
    return data[-1]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    last_element = get_last_item(sample_list)
    print(last_element)
    sample_list_empty = []
    try:
        get_last_item(sample_list_empty)
    except IndexError as e:
        print(f"Error for empty list: {e}")