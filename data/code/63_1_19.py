def get_first_element(data):
    if not data:
        raise IndexError("list is empty")
    return data[0]

if __name__ == '__main__':
    sample_lists = {
        'list1': [1, 2, 3, 4],
        'list2': ['a', 'b', 'c'],
        'empty_list': []
    }
    
    for name, lst in sample_lists.items():
        try:
            print(f"First element of {name}: {get_first_element(lst)}")
        except IndexError as e:
            print(f"Error caught for {name}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")