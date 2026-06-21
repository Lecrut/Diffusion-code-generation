def count_occurrences(lst, target):
    return lst.count(target)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 1]
    target_value = 1
    result = count_occurrences(sample_list, target_value)
    print(result)