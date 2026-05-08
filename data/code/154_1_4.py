def count_list_items(iterable):
    return len(iterable)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple2 = ('a', 'b', 'c')
    empty_list = []
    empty_tuple = ()
    large_list = list(range(1000000))
    print(f"Count of list1: {count_list_items(list1)}")
    print(f"Count of tuple2: {count_list_items(tuple2)}")
    print(f"Count of empty_list: {count_list_items(empty_list)}")
    print(f"Count of empty_tuple: {count_list_items(empty_tuple)}")
    print(f"Count of large_list: {count_list_items(large_list)}")