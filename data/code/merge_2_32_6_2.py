def count_unique_items(iterable):
    unique_set = set(iterable)
    return len(unique_set)
if __name__ == '__main__':
    list1 = [1, 2, 2, 3, 4, 4, 4]
    list2 = ['a', 'b', 'a', 'c', 'b']
    tuple1 = (5, 6, 7, 5)
    string_iterable = "hello"
    print(f"List 1: {list1}, Unique count: {count_unique_items(list1)}")
    print(f"List 2: {list2}, Unique count: {count_unique_items(list2)}")
    print(f"Tuple 1: {tuple1}, Unique count: {count_unique_items(tuple1)}")
    print(f"String Iterable: '{string_iterable}', Unique count: {count_unique_items(string_iterable)}")