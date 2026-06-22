def get_last_item(data_list):
    if not data_list:
        raise IndexError("Cannot retrieve the last item from an empty list")
    return data_list[-1]

if __name__ == '__main__':
    sample_lists = [
        [5, 10, 15, 20],
        [],
        ['a', 'b', 'c'],
        [True, False]
    ]
    
    for idx, lst in enumerate(sample_lists):
        try:
            print(f"Last item of list {idx + 1}: {get_last_item(lst)}")
        except IndexError as e:
            print(f"Error for list {idx + 1}: {e}")