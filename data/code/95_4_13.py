def satisfies_conditions(numbers):
    count = 0
    for value in numbers:
        is_positive = value > 0
        is_even = value % 2 == 0
        is_divisible = value % 2 == 0
        if is_positive and is_even and is_divisible:
            count += 1
    return count >= 3

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_b = [-2, -4, -6, 8, 10]
    list_c = [2, 4, 6]
    list_d = [0, 1, 3, 5, 7]
    result_a = satisfies_conditions(list_a)
    result_b = satisfies_conditions(list_b)
    result_c = satisfies_conditions(list_c)
    result_d = satisfies_conditions(list_d)
    print(result_a)
    print(result_b)
    print(result_c)
    print(result_d)