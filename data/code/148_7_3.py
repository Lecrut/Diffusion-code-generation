def max_element(lst):
    if not lst:
        raise ValueError("List is empty")
    max_val = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
    return max_val

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(max_element(sample_list))