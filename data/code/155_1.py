def calculate_list_sum(iterable):
    total = 0
    for item in iterable:
        total += item
    return total
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple2 = (10, 20, 30)
    empty_list = []
    single_element = [42]
    print(f"Sum of {list1}: {calculate_list_sum(list1)}")
    print(f"Sum of {tuple2}: {calculate_list_sum(tuple2)}")
    print(f"Sum of {empty_list}: {calculate_list_sum(empty_list)}")
    print(f"Sum of {single_element}: {calculate_list_sum(single_element)}")