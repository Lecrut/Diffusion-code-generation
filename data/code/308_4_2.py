def iterative_length(data):
    count = 0
    for item in data:
        count += 1
    return count
if __name__ == '__main__':
    tuple_data = (1, 2, 3, 4, 5)
    list_data = [10, 20, 30, 40]
    length_tuple = iterative_length(tuple_data)
    length_list = iterative_length(list_data)
    print(f"Length of tuple {tuple_data}: {length_tuple}")
    print(f"Length of list {list_data}: {length_list}")