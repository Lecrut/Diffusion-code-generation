def reverse_list(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    reversed_lst = []
    for item in reversed(lst):
        reversed_lst.extend([item])
    return reversed_lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    try:
        reversed_list = reverse_list(sample_list)
        print(reversed_list)
    except ValueError as e:
        print(e)