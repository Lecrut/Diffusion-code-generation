def sum_numerical_contents(data):
    total = 0
    if isinstance(data, (list, tuple)):
        for item in data:
            if isinstance(item, (int, float)):
                total += item
    return total
if __name__ == '__main__':
    list_data = [1, 2.5, 'a', 4, None]
    tuple_data = (10, 20, 'b', 30.5)
    mixed_data = [1, 2, "three", 4.0]
    empty_data = []
    single_item_list = [5]
    single_item_tuple = (99,)
    print(f"Sum of list_data: {sum_numerical_contents(list_data)}")
    print(f"Sum of tuple_data: {sum_numerical_contents(tuple_data)}")
    print(f"Sum of mixed_data: {sum_numerical_contents(mixed_data)}")
    print(f"Sum of empty_data: {sum_numerical_contents(empty_data)}")
    print(f"Sum of single_item_list: {sum_numerical_contents(single_item_list)}")
    print(f"Sum of single_item_tuple: {sum_numerical_contents(single_item_tuple)}")