def check_numbers(numbers):
    count = 0
    for num in numbers:
        is_positive = num > 0
        is_even = num % 2 == 0
        is_divisible_by_2 = num % 2 == 0
        if is_positive and is_even and is_divisible_by_2:
            count += 1
    return count >= 3
if __name__ == '__main__':
    sample_list1 = [2, 4, 6, 1, 3, 5]
    sample_list2 = [1, 3, 5, 7, 9]
    sample_list3 = [2, 4, 6, 8, 10]
    sample_list4 = [10, 20, 30, 40]
    print(check_numbers(sample_list1))
    print(check_numbers(sample_list2))
    print(check_numbers(sample_list3))
    print(check_numbers(sample_list4))