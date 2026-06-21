def remove_duplicates(lst, value):
    result = []
    for item in lst:
        if item != value:
            result.append(item)
    return result

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 3, 2, 5]
    value_to_remove = 3
    result = remove_duplicates(sample_list, value_to_remove)
    print(result)