def validate_input(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if not lst:
        raise ValueError("List cannot be empty")

def find_max(lst):
    validate_input(lst)
    max_elem = lst[0]
    for elem in lst[1:]:
        if elem > max_elem:
            max_elem = elem
    return max_elem

if __name__ == '__main__':
    sample_list = [7, 2, 9, 5, 3, 8]
    print(find_max(sample_list))