def find_maximum(lst):
    max_elem = lst[0]
    for elem in lst:
        if elem > max_elem:
            max_elem = elem
    return max_elem

if __name__ == '__main__':
    sample_list = [45, 12, 89, 34, 76, 100]
    print(find_maximum(sample_list))