def count_non_tuples(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    
    non_tuple_count = 0
    for element in lst:
        if not isinstance(element, tuple):
            non_tuple_count += 1
    
    return non_tuple_count

if __name__ == '__main__':
    sample_list = [1, "apple", (3, 4), [5, 6], "banana"]
    non_tuple_count = count_non_tuples(sample_list)
    print(non_tuple_count)