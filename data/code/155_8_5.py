def sum_of_absolute_values(data):
    total_sum = 0
    for x in data:
        total_sum += abs(x)
    return total_sum
if __name__ == '__main__':
    sample_list_1 = [1, -2, 3, -4, 5]
    result_1 = sum_of_absolute_values(sample_list_1)
    print(result_1)
    sample_list_2 = [-10, 0, -5, 20]
    result_2 = sum_of_absolute_values(sample_list_2)
    print(result_2)
    sample_list_3 = [-1, -2, -3]
    result_3 = sum_of_absolute_values(sample_list_3)
    print(result_3)