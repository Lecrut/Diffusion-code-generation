def get_last_item(data_list):
    if not data_list:
        raise IndexError("Cannot get the last item from an empty list")
    return data_list[-1]

if __name__ == '__main__':
    sample_values = {
        'list_with_items': [1, 2, 3, 4, 5],
        'empty_list': []
    }
    
    for name, lst in sample_values.items():
        try:
            last_item = get_last_item(lst)
            print(f"Last item of {name}: {last_item}")
        except IndexError as e:
            print(f"Error for {name}: {e}")