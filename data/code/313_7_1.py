def contains_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return True
    return False
if __name__ == '__main__':
    sample_list = [1, 3, 5, 7, 9, 11, 13, 15, 20]
    result = contains_even(sample_list)
    print(result)
    sample_list_2 = [1, 3, 5, 7, 9, 11]
    result_2 = contains_even(sample_list_2)
    print(result_2)
    sample_list_3 = [101, 103, 105, 107]
    result_3 = contains_even(sample_list_3)
    print(result_3)