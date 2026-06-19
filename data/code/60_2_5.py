def get_last_item(data_list):
    if not data_list:
        raise IndexError("Cannot retrieve the last item from an empty list")
    return data_list[-1]

if __name__ == '__main__':
    sample_lists = [
        [5, 10, 15, 20],
        [],
        ['a', 'b', 'c'],
        [True, False, None]
    ]

    for index, lst in enumerate(sample_lists):
        try:
            last_item = get_last_item(lst)
            print(f"Last item of list {index + 1}: {last_item}")
        except IndexError as e:
            print(f"Error for list {index + 1}: {e}")