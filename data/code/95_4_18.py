def is_positive(num):
    return num > 0

def is_even(num):
    return num % 2 == 0

def check_numbers(numbers):
    count = sum(is_positive(num) and is_even(num) for num in numbers)
    return count >= 3

if __name__ == '__main__':
    sample_list1 = [2, 4, 6, 1, 3, 5]
    sample_list2 = [1, 3, 5, 7, 9]
    sample_list3 = [2, 4, 6, 8, 10]
    sample_list4 = [2, 4, 1, 3]
    print(check_numbers(sample_list1))
    print(check_numbers(sample_list2))
    print(check_numbers(sample_list3))
    print(check_numbers(sample_list4))