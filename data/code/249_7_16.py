def validate_input(lst):
    if not lst:
        raise ValueError("List is empty")

def find_max(lst):
    max_elem = lst[0]
    for elem in lst[1:]:
        if elem > max_elem:
            max_elem = elem
    return max_elem

if __name__ == '__main__':
    sample_list = [7, 2, 9, 5, 3, 8]
    validate_input(sample_list)
    print(find_max(sample_list))