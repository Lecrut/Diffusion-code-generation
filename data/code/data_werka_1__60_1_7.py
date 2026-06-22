def get_last_item(data):
    if not data:
        raise IndexError("list is empty")
    return data[-1]

if __name__ == '__main__':
    sample_lists = [
        [10, 20, 30],
        ['hello', 'world'],
        [True, False],
        [],
        [42]
    ]
    
    for i, lst in enumerate(sample_lists):
        try:
            print(f"Last item of list {i+1}: {get_last_item(lst)}")
        except IndexError as e:
            print(f"Error for list {i+1}: {e}")