def find_min_element(t):
    min_val = t[0]
    for val in t:
        if val < min_val:
            min_val = val
    return min_val

if __name__ == '__main__':
    sample_tuple = (5, 3, 9, 1, 7)
    print(find_min_element(sample_tuple))