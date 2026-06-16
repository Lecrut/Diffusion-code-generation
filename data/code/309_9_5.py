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
    float_tuple = (1.5, 2.5)
    print(f"Sum of list1: {sum_container(list1)}")
    print(f"Sum of tuple2: {sum_container(tuple2)}")
    print(f"Sum of mixed_list: {sum_container(mixed_list)}")
    print(f"Sum of empty_list: {sum_container(empty_list)}")
    print(f"Sum of float_tuple: {sum_container(float_tuple)}")