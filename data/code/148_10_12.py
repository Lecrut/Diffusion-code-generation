def find_max_element(lst):
    if not lst:
        return None
    max_elem = lst[0]
    for elem in lst[1:]:
        if elem > max_elem:
            max_elem = elem
    return max_elem
if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_max_element(sample_list))