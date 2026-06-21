def reverse_list_with_validation(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    return lst[::-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list_with_validation(sample_list)
    print(reversed_list)