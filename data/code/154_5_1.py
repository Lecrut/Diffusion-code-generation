def count_occurrences(data_list, target_value):
    count = 0
    for item in data_list:
        if item == target_value:
            count += 1
    return count
if __name__ == '__main__':
    sample_list = [1, 2, 3, 2, 4, 2, 5, 2, 1]
    target = 2
    result = count_occurrences(sample_list, target)
    print(result)