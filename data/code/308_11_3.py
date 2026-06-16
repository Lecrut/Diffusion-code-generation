def count_sequence_items(iterable):
    return len(iterable)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple2 = ('a', 'b', 'c')
    empty_list = []
    single_item = (99,)
    print(f"Count for list1: {count_sequence_items(list1)}")
    print(f"Count for tuple2: {count_sequence_items(tuple2)}")
    print(f"Count for empty_list: {count_sequence_items(empty_list)}")
    print(f"Count for single_item: {count_sequence_items(single_item)}")