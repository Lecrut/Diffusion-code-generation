def find_max(lst):
    if not lst:
        raise ValueError("List is empty")
    max_element = lst[0]
    for element in lst[1:]:
        if element > max_element:
            max_element = element
    return max_element

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_max(sample_list))