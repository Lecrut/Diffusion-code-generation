def retrieve_middle_item(data):
    size = len(data)
    if size == 0:
        raise ValueError("Input sequence must not be empty")
    center_position = size // 2
    if size % 2 != 0:
        return data[center_position]
    else:
        return data[center_position - 1]

if __name__ == '__main__':
    odd_length_list = [10, 20, 30, 40, 50]
    print(retrieve_middle_item(odd_length_list))

    even_length_list = [1, 2, 3, 4]
    print(retrieve_middle_item(even_length_list))

    single_item_list = [99]
    print(retrieve_middle_item(single_item_list))

    two_item_list = [5, 6]
    print(retrieve_middle_item(two_item_list))

    odd_string = "Python"
    print(retrieve_middle_item(odd_string))

    even_string = "Java"
    print(retrieve_middle_item(even_string))

    odd_tuple = (1, 2, 3)
    print(retrieve_middle_item(odd_tuple))

    even_tuple = (1, 2, 3, 4)
    print(retrieve_middle_item(even_tuple))

    large_odd_sequence = list(range(1, 101))
    print(retrieve_middle_item(large_odd_sequence))

    large_even_sequence = list(range(1, 100))
    print(retrieve_middle_item(large_even_sequence))