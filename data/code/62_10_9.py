def validate_list_length(lst):
    return len(lst) >= 2

def get_second_item(lst):
    if not validate_list_length(lst):
        return None
    return lst[1]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3],
        ['a', 'b'],
        [True, False, True],
        [],
        [42]
    ]
    
    for i, lst in enumerate(sample_lists):
        print(f"Sample list {i+1}: {lst}")
        second_item = get_second_item(lst)
        print(f"The second item is: {second_item}")