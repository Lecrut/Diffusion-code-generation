def list_item_counter(iterable):
    return len(iterable)
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = ['a', 'b', 'c']
    sample_tuple = (10, 20, 30)
    sample_empty = []
    sample_string = "hello"
    print(f"Count for {sample_list_1}: {list_item_counter(sample_list_1)}")
    print(f"Count for {sample_list_2}: {list_item_counter(sample_list_2)}")
    print(f"Count for {sample_tuple}: {list_item_counter(sample_tuple)}")
    print(f"Count for {sample_empty}: {list_item_counter(sample_empty)}")
    print(f"Count for '{sample_string}': {list_item_counter(sample_string)}")