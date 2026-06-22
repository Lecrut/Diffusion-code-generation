def find_min_max(tup):
    if len(tup) == 0:
        return None, None
    min_val = tup[0]
    max_val = tup[0]
    for num in tup[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return min_val, max_val

if __name__ == '__main__':
    sample_tuple = (3, 5, 1, 8, 2)
    print(find_min_max(sample_tuple))