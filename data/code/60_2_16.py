def get_last_item(data_list):
    if not data_list:
        raise IndexError("Cannot retrieve last item from an empty list")
    return data_list[-1]

if __name__ == '__main__':
    sample_lists = [
        [10, 20, 30, 40],
        [],
        ['a', 'b', 'c'],
        [True, False]
    ]
    
    for idx, lst in enumerate(sample_lists):
        try:
            last_item = get_last_item(lst)
            print(f"Last item of list {idx + 1}: {last_item}")
        except IndexError as e:
            print(f"Error for list {idx + 1}: {e}")