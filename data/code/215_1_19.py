def find_max_value(tup):
    max_val = tup[0]
    for val in tup:
        if val > max_val:
            max_val = val
    return max_val

if __name__ == '__main__':
    sample_tuple = (99, 45, 67, 12, 88)
    print(find_max_value(sample_tuple))