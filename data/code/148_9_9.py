def find_largest(lst):
    if not lst:
        raise ValueError("List is empty")
    largest = lst[0]
    for item in lst[1:]:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    sample_list = [3, 5, 1, 8, 2]
    print(find_largest(sample_list))