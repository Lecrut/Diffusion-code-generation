def print_iterable_with_separation(iterable):
    for item in iterable:
        print(item)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple2 = ('a', 'b', 'c', 'd')
    list3 = [10.5, 20.1, 30.9]
    print("--- List 1 ---")
    print_iterable_with_separation(list1)
    print("\n--- Tuple 2 ---")
    print_iterable_with_separation(tuple2)
    print("\n--- List 3 ---")
    print_iterable_with_separation(list3)