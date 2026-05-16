def sum_of_absolute_values(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += abs(number)
    return total_sum
if __name__ == '__main__':
    sample_list = [1, -2, 3, -4, 5]
    result = sum_of_absolute_values(sample_list)
    print(result)