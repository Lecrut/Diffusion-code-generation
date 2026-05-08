def list_item_counter(iterable):
    return len(iterable)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    sample_tuple = ('a', 'b', 'c')
    sample_empty = []
    sample_string = "hello"
    print(f"Count of {sample_list}: {list_item_counter(sample_list)}")
    print(f"Count of {sample_tuple}: {list_item_counter(sample_tuple)}")
    print(f"Count of {sample_empty}: {list_item_counter(sample_empty)}")
    print(f"Count of {sample_string}: {list_item_counter(sample_string)}")