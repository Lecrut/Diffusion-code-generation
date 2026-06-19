def get_last_item(data_list):
    if not data_list:
        raise IndexError("Cannot retrieve the last item from an empty list")
    return data_list[-1]

if __name__ == '__main__':
    sample_values = [
        [1, 2, 3, 4, 5],
        [],
        ['a', 'b', 'c'],
        [True, False]
    ]

    for idx, value_list in enumerate(sample_values):
        try:
            last_item = get_last_item(value_list)
            print(f"Last item of list {idx + 1}: {last_item}")
        except IndexError as e:
            print(f"Error for list {idx + 1}: {e}")