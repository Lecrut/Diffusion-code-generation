def find_largest(lst):
    if not lst:
        return None
    largest = lst[0]
    for element in lst[1:]:
        if element > largest:
            largest = element
    return largest

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_largest(sample_list))