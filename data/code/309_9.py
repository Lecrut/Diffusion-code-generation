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
    tuple_data = (10, -5, 'hello', 3.14)
    mixed_data = [1, 2, "three", 4.0]
    empty_data = []
    non_container = 100
    print(f"Sum of list_data: {sum_container(list_data)}")
    print(f"Sum of tuple_data: {sum_container(tuple_data)}")
    print(f"Sum of mixed_data: {sum_container(mixed_data)}")
    print(f"Sum of empty_data: {sum_container(empty_data)}")
    print(f"Sum of non_container (should be 0): {sum_container(non_container)}")