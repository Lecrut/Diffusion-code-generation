def combine_conditions(numbers, condition1, condition2):
    return [num for num in numbers if condition1(num) and condition2(num)]

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    condition_a = lambda x: x % 2 == 0
    condition_b = lambda x: x > 5
    combined_list = combine_conditions(data, condition_a, condition_b)
    print(combined_list)