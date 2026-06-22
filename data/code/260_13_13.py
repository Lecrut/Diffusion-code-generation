def is_subset(set1, set2):
    if not all(isinstance(x, (int, float)) for x in set1) or not all(isinstance(x, (int, float)) for x in set2):
        raise ValueError("Both inputs must be sets of numbers.")
    return set1.issubset(set2)

if __name__ == '__main__':
    data1 = {1, 3, 5, 8}
    data2 = {5, 1, 3, 8, 9}
    result = is_subset(data1, data2)
    print(result)