def count_items(iterable):
    if not isinstance(iterable, (list, tuple, set)):
        raise ValueError("Input must be a list, tuple, or set")
    item_count = {}
    for item in iterable:
        item_count[item] = item_count.get(item, 0) + 1
    return item_count

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 3]
    sample_tuple = (10, 20, 30, 10)
    sample_set = {100, 200, 300, 100}
    
    print(f"Count in {sample_list}: {count_items(sample_list)}")
    print(f"Count in {sample_tuple}: {count_items(sample_tuple)}")
    print(f"Count in {sample_set}: {count_items(sample_set)}")