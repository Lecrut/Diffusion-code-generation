def check_all_positive(numbers):
    all_positive = True
    for num in numbers:
        if num <= 0:
            all_positive = False
            break
    return all_positive

if __name__ == '__main__':
    sample_values_1 = [6, 7, 8, 9, 10]
    result_1 = check_all_positive(sample_values_1)
    print(result_1)

    sample_values_2 = [-1, 2, 3, 4, 5]
    result_2 = check_all_positive(sample_values_2)
    print(result_2)