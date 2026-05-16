def count_list_items(iterable):
    return len(iterable)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple2 = ('a', 'b', 'c', 'd')
    empty_list = []
    empty_tuple = ()
    print(f"Count for list1: {count_list_items(list1)}")
    print(f"Count for tuple2: {count_list_items(tuple2)}")
    print(f"Count for empty_list: {count_list_items(empty_list)}")
    print(f"Count for empty_tuple: {count_list_items(empty_tuple)}")