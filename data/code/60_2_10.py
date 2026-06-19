def get_last_item(data_list):
    if not data_list:
        raise IndexError("Cannot get the last item from an empty list")
    return data_list[-1]

if __name__ == '__main__':
    sample_lists = [
        [5, 10, 15, 20],
        ['a', 'b', 'c'],
        [],
        [3.14, 2.71]
    ]
    
    for i, lst in enumerate(sample_lists):
        try:
            last_item = get_last_item(lst)
            print(f"Last item of list {i + 1}: {last_item}")
        except IndexError as e:
            print(f"Error for list {i + 1}: {e}")