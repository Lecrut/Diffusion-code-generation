def calculate_differences(list1, list2):
    differences = {}
    for index in range(min(len(list1), len(list2))):
        difference_value = list1[index] - list2[index]
        differences[index] = difference_value
    return differences

if __name__ == '__main__':
    sample_list1 = [100, 200, 300, 400]
    sample_list2 = [50, 75, 100, 125]
    result_differences = calculate_differences(sample_list1, sample_list2)
    print(result_differences)