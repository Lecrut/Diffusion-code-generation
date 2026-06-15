def list_sum(iterable):
    return sum(iterable)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(f"Sum of {list1}: {list_sum(list1)}")
    list2 = [10, -5, 20.5, 0]
    print(f"Sum of {list2}: {list_sum(list2)}")
    empty_list = []
    print(f"Sum of {empty_list}: {list_sum(empty_list)}")
    tuple_data = (100, 200, 300)
    print(f"Sum of {tuple_data}: {list_sum(tuple_data)}")