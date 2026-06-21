def is_valid_list(lst):
    return isinstance(lst, list)

def reverse_list_with_extend(lst):
    if not is_valid_list(lst):
        raise ValueError("Input must be a list")
    
    reversed_lst = []
    for item in reversed(lst):
        reversed_lst.extend([item])
    return reversed_lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list_with_extend(sample_list)
    print(reversed_list)