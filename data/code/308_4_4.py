def count_length_iterative(data):
    count = 0
    for item in data:
        count += 1
    return count
if __name__ == '__main__':
    tuple_data = (1, 2, 3, 4, 5)
    list_data = [10, 20, 30, 40]
    empty_tuple = ()
    empty_list = []
    length_tuple = count_length_iterative(tuple_data)
    length_list = count_length_iterative(list_data)
    length_empty_tuple = count_length_iterative(empty_tuple)
    length_empty_list = count_length_iterative(empty_list)
    print(f"Length of {tuple_data}: {length_tuple}")
    print(f"Length of {list_data}: {length_list}")
    print(f"Length of {empty_tuple}: {length_empty_tuple}")
    print(f"Length of {empty_list}: {length_empty_list}")