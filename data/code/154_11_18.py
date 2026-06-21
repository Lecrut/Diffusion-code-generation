def count_items(iterable):
    if not isinstance(iterable, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    
    item_count = {}
    for item in iterable:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    return item_count

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = ['a', 'b', 'c']
    sample_tuple = (10, 20, 30)
    sample_empty = []
    
    print(f"Count for {sample_list_1}: {count_items(sample_list_1)}")
    print(f"Count for {sample_list_2}: {count_items(sample_list_2)}")
    print(f"Count for {sample_tuple}: {count_items(sample_tuple)}")
    print(f"Count for {sample_empty}: {count_items(sample_empty)}")