def count_items_in_tuple(tup):
    if not isinstance(tup, tuple):
        raise TypeError("Input must be a tuple")
    
    count = 0
    for _ in tup:
        count += 1
    
    return count

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    print(count_items_in_tuple(sample_tuple))