def count_occurrences(data, target):
    count = 0
    for item in data:
        if item == target:
            count += 1
    return count
if __name__ == '__main__':
    my_list = [1, 2, 3, 2, 4, 2, 5, 2]
    target_value = 2
    result = count_occurrences(my_list, target_value)
    print(result)