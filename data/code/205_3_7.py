def sort_tuple_to_list(tup):
    sorted_list = []
    while tup:
        min_val = min(tup)
        sorted_list.append(min_val)
        tup = tup[:tup.index(min_val)] + tup[tup.index(min_val) + 1:]
    return sorted_list

if __name__ == '__main__':
    sample_tuple = (5, 3, 9, 1, 4)
    print(sort_tuple_to_list(sample_tuple))