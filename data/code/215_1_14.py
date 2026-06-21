def find_max_value(tup):
    max_val = tup[0]
    for num in tup:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    sample_tuple = (99, 45, 67, 12, 88)
    print(find_max_value(sample_tuple))