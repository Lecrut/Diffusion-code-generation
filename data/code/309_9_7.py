def sum_container(data):
    total = 0
    if isinstance(data, (list, tuple)):
        for item in data:
            if isinstance(item, (int, float)):
                total += item
    return total
if __name__ == '__main__':
    list1 = [1, 2, 'a', 3.5, None]
    tuple2 = (10, 20, 'b', 40)
    mixed_list = [5, 10, "hello", 15]
    empty_list = []
    empty_tuple = ()
    print(f"Sum of list1: {sum_container(list1)}")
    print(f"Sum of tuple2: {sum_container(tuple2)}")
    print(f"Sum of mixed_list: {sum_container(mixed_list)}")
    print(f"Sum of empty_list: {sum_container(empty_list)}")
    print(f"Sum of empty_tuple: {sum_container(empty_tuple)}")