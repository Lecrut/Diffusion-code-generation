def find_middle(data):
    middle_index = len(data) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_list1 = [5, 10, 15, 20, 25]
    sample_list2 = [100, 200, 300, 400]
    sample_list3 = [7]
    sample_list4 = [2, 4, 6, 8]

    middle_value1 = find_middle(sample_list1)
    middle_value2 = find_middle(sample_list2)
    middle_value3 = find_middle(sample_list3)
    middle_value4 = find_middle(sample_list4)

    print(middle_value1)
    print(middle_value2)
    print(middle_value3)
    print(middle_value4)