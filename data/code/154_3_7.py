def count_occurrences(lst, target):
    return lst.count(target)

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 2, 2, 3]
    value_to_count = 2
    result = count_occurrences(data, value_to_count)
    print(result)