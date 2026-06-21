def reverse_using_iter(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    return list(reversed(lst))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_using_iter(sample_list)
    print(reversed_list)