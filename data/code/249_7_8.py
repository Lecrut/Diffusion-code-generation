def find_max(lst):
    if not lst:
        raise ValueError("List is empty")
    current_max = lst[0]
    for element in lst[1:]:
        if element > current_max:
            current_max = element
    return current_max

if __name__ == '__main__':
    sample_list = [4, 7, 2, 9, 6, 3, 5, 8]
    print(find_max(sample_list))