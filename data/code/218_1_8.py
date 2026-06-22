def find_min_element(tup):
    min_val = tup[0]
    for element in tup:
        if element < min_val:
            min_val = element
    return min_val

if __name__ == '__main__':
    sample_tuple = (5, 3, 9, 1, 7)
    print(find_min_element(sample_tuple))