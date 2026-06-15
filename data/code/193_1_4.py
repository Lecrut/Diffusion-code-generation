def calculate_list_sum(iterable):
    return sum(iterable)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(calculate_list_sum(list1))
    list2 = [10, -5, 20.5, 0]
    print(calculate_list_sum(list2))
    empty_list = []
    print(calculate_list_sum(empty_list))
    tuple1 = (100, 200)
    print(calculate_list_sum(tuple1))