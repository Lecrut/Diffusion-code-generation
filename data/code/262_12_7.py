def find_extremes(tup):
    if len(tup) == 0:
        return None, None
    smallest = largest = tup[0]
    for num in tup[1:]:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    return smallest, largest

if __name__ == '__main__':
    sample_tuple = (3, 5, 1, 8, 2)
    print(find_extremes(sample_tuple))