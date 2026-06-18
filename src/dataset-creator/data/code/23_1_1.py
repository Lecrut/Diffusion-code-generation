def count_set_items(iterable):
    return len(iterable)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple2 = ('a', 'b', 'c')
    empty_list = []
    large_list = list(range(1000000))
    print(f"Count for {list1}: {count_set_items(list1)}")
    print(f"Count for {tuple2}: {count_set_items(tuple2)}")
    print(f"Count for {empty_list}: {count_set_items(empty_list)}")
    print(f"Count for large list: {count_set_items(large_list)}")