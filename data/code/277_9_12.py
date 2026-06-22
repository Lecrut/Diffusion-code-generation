def count_items_in_tuple(tup):
    count = 0
    for item in tup:
        count += 1
    return count

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    print(count_items_in_tuple(sample_tuple))