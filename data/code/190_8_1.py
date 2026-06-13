def check_membership(data_list, item):
    if isinstance(data_list, (list, tuple, set)):
        return item in data_list
    else:
        try:
            return item in data_list
        except TypeError:
            return False
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    item1 = 8
    print(f"List: {list1}, Item: {item1}")
    result1_builtin = item1 in list1
    result1_manual = False
    for element in list1:
        if element == item1:
            result1_manual = True
            break
    print(f"Built-in 'in' result: {result1_builtin}")
    print(f"Manual loop result: {result1_manual}")
    list2 = ['a', 'b', 'c', 'd']
    item2 = 'c'
    print(f"\nList: {list2}, Item: {item2}")
    result2_builtin = item2 in list2
    result2_manual = False
    for element in list2:
        if element == item2:
            result2_manual = True
            break
    print(f"Built-in 'in' result: {result2_builtin}")
    print(f"Manual loop result: {result2_manual}")
    import timeit
    setup = "from __main__ import list1, item1, list2, item2"
    time_builtin = timeit.timeit("item1 in list1", setup=setup, number=100000)
    time_manual = timeit.timeit("any(x == item1 for x in list1)", setup=setup, number=100000)
    print("\nPerformance comparison (100,000 runs):")
    print(f"Built-in 'in' operator time: {time_builtin:.6f} seconds")
    print(f"Manual loop time: {time_manual:.6f} seconds")