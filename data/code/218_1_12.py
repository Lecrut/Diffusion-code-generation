def find_min_element(tup):
    min_val = tup[0]
    for num in tup:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_tuple = (5, 3, 9, 1, 4)
    print(find_min_element(sample_tuple))