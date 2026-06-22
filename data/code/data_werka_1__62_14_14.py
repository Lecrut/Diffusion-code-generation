def get_second_item(data):
    if len(data) < 2:
        return None
    return data[1]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3],
        ['a', 'b'],
        [],
        [42],
        [True, False, True]
    ]
    
    for i, lst in enumerate(sample_lists):
        print(f"List {i+1}: {get_second_item(lst)}")