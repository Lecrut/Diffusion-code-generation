def find_extremes(tup):
    smallest = tup[0]
    largest = tup[0]
    for num in tup:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    return smallest, largest

if __name__ == '__main__':
    sample_tuple = (34, 12, 98, 56, 78)
    print(find_extremes(sample_tuple))