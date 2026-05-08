def sum_of_absolute_values(numbers):
    total = 0
    for number in numbers:
        total += abs(number)
    return total
if __name__ == '__main__':
    sample_list1 = [1, -2, 3, -4, 5]
    result1 = sum_of_absolute_values(sample_list1)
    print(result1)
    sample_list2 = [-10, 0, -5, 15]
    result2 = sum_of_absolute_values(sample_list2)
    print(result2)
    sample_list3 = [7, 7, 7]
    result3 = sum_of_absolute_values(sample_list3)
    print(result3)
    sample_list4 = [-1, -2, -3]
    result4 = sum_of_absolute_values(sample_list4)
    print(result4)