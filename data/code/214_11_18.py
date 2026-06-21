def find_min_element(lst):
    if not lst:
        return None
    min_elem = lst[0]
    for elem in lst[1:]:
        if elem < min_elem:
            min_elem = elem
    return min_elem

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_min_element(sample_list))