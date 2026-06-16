def contains_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return True
    return False
if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9, 11, 13, 15, 20]
    result = contains_even(sample_list)
    print(result)
    sample_list_no_even = [1, 3, 5, 7, 9, 11, 13, 15]
    result_no_even = contains_even(sample_list_no_even)
    print(result_no_even)
    sample_list_all_even = [2, 4, 6, 8]
    result_all_even = contains_even(sample_list_all_even)
    print(result_all_even)