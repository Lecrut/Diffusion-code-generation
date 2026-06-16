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
    tuple_data = (10, 20, 'b', 30.5)
    mixed_data = [1, "two", 3, None, 5.5]
    empty_data = []
    float_only = (1.1, 2.2)
    print(f"Sum of list_data: {sum_container(list_data)}")
    print(f"Sum of tuple_data: {sum_container(tuple_data)}")
    print(f"Sum of mixed_data: {sum_container(mixed_data)}")
    print(f"Sum of empty_data: {sum_container(empty_data)}")
    print(f"Sum of float_only: {sum_container(float_only)}")