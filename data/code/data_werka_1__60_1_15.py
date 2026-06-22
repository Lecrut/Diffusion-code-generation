def get_last_item(data):
    try:
        return data[-1]
    except IndexError:
        raise ValueError("list is empty")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    last_element = get_last_item(sample_list)
    print(f"Last element: {last_element}")

    empty_list = []
    try:
        get_last_item(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")