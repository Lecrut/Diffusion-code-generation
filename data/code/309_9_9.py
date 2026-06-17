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
    list_data = [1, 2.5, 'a', 4]
    tuple_data = (10, -5, 'b', 3.5)
    mixed_data = [1, 2, 'three', 4]
    empty_data = []
    non_container = 100
    print(f"Sum of list {list_data}: {sum_container(list_data)}")
    print(f"Sum of tuple {tuple_data}: {sum_container(tuple_data)}")
    print(f"Sum of mixed list {mixed_data}: {sum_container(mixed_data)}")
    print(f"Sum of empty list {empty_data}: {sum_container(empty_data)}")
    print(f"Sum of non-container {non_container}: {sum_container(non_container)}")