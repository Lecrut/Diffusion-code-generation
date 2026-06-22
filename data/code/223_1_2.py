def find_largest_element(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

if __name__ == '__main__':
    sample_list = [3.14, 2.71, 1.618, 0.577, 1.414]
    print(find_largest_element(sample_list))