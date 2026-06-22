def get_last_item(data_list):
    if not data_list:
        raise IndexError("Cannot get the last item from an empty list")
    return data_list[-1]

if __name__ == '__main__':
    sample_values = [
        [5, 10, 15, 20],
        [],
        ['a', 'b', 'c'],
        [True, False, True]
    ]
    
    for i, lst in enumerate(sample_values):
        try:
            print(f"Last item of list {i+1}: {get_last_item(lst)}")
        except IndexError as e:
            print(f"Error for list {i+1}: {e}")