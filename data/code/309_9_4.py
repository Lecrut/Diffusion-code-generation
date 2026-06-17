def sum_container(data):
    total = 0
    if isinstance(data, (list, tuple)):
        for item in data:
            try:
                total += float(item)
            except (ValueError, TypeError):
                pass
    return total
if __name__ == '__main__':
    list_data = [1, 2.5, 'a', 4, None]
    tuple_data = (10, 20, '3.5', 'error')
    mixed_data = [5, 10, "hello", 15.5]
    empty_list = []
    empty_tuple = ()
    print(f"Sum of list {list_data}: {sum_container(list_data)}")
    print(f"Sum of tuple {tuple_data}: {sum_container(tuple_data)}")
    print(f"Sum of mixed list {mixed_data}: {sum_container(mixed_data)}")
    print(f"Sum of empty list {empty_list}: {sum_container(empty_list)}")
    print(f"Sum of empty tuple {empty_tuple}: {sum_container(empty_tuple)}")