def count_sequence_items(iterable):
    return len(iterable)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple2 = (6, 7, 8, 9)
    empty_list = []
    string_tuple = "hello"
    print(f"Count for list1: {count_sequence_items(list1)}")
    print(f"Count for tuple2: {count_sequence_items(tuple2)}")
    print(f"Count for empty_list: {count_sequence_items(empty_list)}")
    print(f"Count for string_tuple: {count_sequence_items(string_tuple)}")