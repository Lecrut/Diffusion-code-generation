def reverse_list(data_list):
    if not isinstance(data_list, list):
        raise ValueError("Input must be a list")
    return list(reversed(data_list))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(f"Original list: {sample_list}")
    reversed_list = reverse_list(sample_list)
    print(f"Reversed list: {reversed_list}")

    sample_list_2 = ['a', 'b', 'c', 'd']
    print(f"Original list: {sample_list_2}")
    reversed_list_2 = reverse_list(sample_list_2)
    print(f"Reversed list: {reversed_list_2}")