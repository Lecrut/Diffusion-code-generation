def calculate_set_sum(data):
    total = 0
    for item in data:
        total += item
    return total
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple2 = (10, 20, 30, 40)
    large_list = list(range(1000000))
    empty_list = []
    print(f"Sum of {list1}: {calculate_set_sum(list1)}")
    print(f"Sum of {tuple2}: {calculate_set_sum(tuple2)}")
    print(f"Sum of large list: {calculate_set_sum(large_list)}")
    print(f"Sum of empty list: {calculate_set_sum(empty_list)}")