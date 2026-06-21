def sort_tuple_to_list(tup):
    sorted_list = []
    while tup:
        min_val = min(tup)
        sorted_list.append(min_val)
        tup = tup.replace((min_val,), ())
    return sorted_list

if __name__ == '__main__':
    sample_tuple = (5, 3, 9, 1, 7)
    print(sort_tuple_to_list(sample_tuple))