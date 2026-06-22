def count_items_in_tuple(tup):
    count = 0
    for item in tup:
        count += 1
    return count

if __name__ == '__main__':
    sample_tuple = (6, 7, 8, 9, 10, 11)
    result = count_items_in_tuple(sample_tuple)
    print(result)