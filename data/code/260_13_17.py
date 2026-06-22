def is_subset(set1, set2):
    return set1.issubset(set2)

if __name__ == '__main__':
    data1 = {1, 3, 5, 8}
    data2 = {1, 2, 3, 4, 5, 6, 7, 8}
    result = is_subset(data1, data2)
    print(result)