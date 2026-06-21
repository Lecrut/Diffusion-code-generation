def count_list_items(iterable):
    if not isinstance(iterable, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    
    counts = {}
    for item in iterable:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    
    return counts

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple2 = ('a', 'b', 'c', 'd')
    empty_list = []
    single_item = [99]

    print(f"Count for list1: {count_list_items(list1)}")
    print(f"Count for tuple2: {count_list_items(tuple2)}")
    print(f"Count for empty_list: {count_list_items(empty_list)}")
    print(f"Count for single_item: {count_list_items(single_item)}")