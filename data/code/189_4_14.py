def remove_duplicates(lst, value):
    result = []
    for item in lst:
        if item != value:
            result.append(item)
    return result

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    value_to_remove_1 = 3
    result_1 = remove_duplicates(sample_list_1, value_to_remove_1)
    print(result_1)

    sample_list_2 = ['a', 'b', 'c', 'd', 'e']
    value_to_remove_2 = 'c'
    result_2 = remove_duplicates(sample_list_2, value_to_remove_2)
    print(result_2)

    sample_list_3 = [10, 20, 30, 40, 50, 30]
    value_to_remove_3 = 30
    result_3 = remove_duplicates(sample_list_3, value_to_remove_3)
    print(result_3)