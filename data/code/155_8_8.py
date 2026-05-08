def sum_of_absolute_values(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += abs(number)
    return total_sum
if __name__ == '__main__':
    sample_list1 = [1, -2, 3, -4, 5]
    sample_list2 = [-10, 0, 5, -2.5]
    sample_list3 = [7, 8, -1, -9]
    sample_list4 = []
    result1 = sum_of_absolute_values(sample_list1)
    result2 = sum_of_absolute_values(sample_list2)
    result3 = sum_of_absolute_values(sample_list3)
    result4 = sum_of_absolute_values(sample_list4)
    print(f"Result for {sample_list1}: {result1}")
    print(f"Result for {sample_list2}: {result2}")
    print(f"Result for {sample_list3}: {result3}")
    print(f"Result for {sample_list4}: {result4}")