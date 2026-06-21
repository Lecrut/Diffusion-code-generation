def find_maximum(lst):
    if not lst:
        raise ValueError("List is empty")
    max_elem = lst[0]
    for elem in lst:
        if elem > max_elem:
            max_elem = elem
    return max_elem

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_maximum(sample_list))