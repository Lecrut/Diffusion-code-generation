def sort_tuple_to_list(tup):
    sorted_list = []
    while tup:
        min_value = min(tup)
        sorted_list.append(min_value)
        tup = tup[:tup.index(min_value)] + tup[tup.index(min_value) + 1:]
    return sorted_list

if __name__ == '__main__':
    sample_tuple = (5, 3, 8, 4, 2)
    print(sort_tuple_to_list(sample_tuple))