def sum_of_numbers(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    result1 = sum_of_numbers(sample_list1)
    print(f"Sum of {sample_list1}: {result1}")

    sample_list2 = [-10, 20, -30, 40]
    result2 = sum_of_numbers(sample_list2)
    print(f"Sum of {sample_list2}: {result2}")