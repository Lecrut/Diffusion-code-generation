def is_valid_list(lst):
    if not isinstance(lst, list) or not lst:
        raise ValueError("Input must be a non-empty list")

def find_max(lst):
    is_valid_list(lst)
    max_elem = lst[0]
    for elem in lst[1:]:
        if elem > max_elem:
            max_elem = elem
    return max_elem

if __name__ == '__main__':
    sample_list = [7, 2, 9, 5, 3, 8]
    print(find_max(sample_list))