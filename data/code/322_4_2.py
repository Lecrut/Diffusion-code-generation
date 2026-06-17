def divide_list(data, divisor):
    for number in data:
        if divisor != 0:
            yield number / divisor
if __name__ == '__main__':
    input_list = [10, 20, 30, 40, 50]
    divisor = 5
    result_generator = divide_list(input_list, divisor)
    results = list(result_generator)
    print(results)
    input_list_with_zero = [10, 20, 0, 40, 50]
    divisor_two = 0
    result_generator_two = divide_list(input_list_with_zero, divisor_two)
    results_two = list(result_generator_two)
    print(results_two)
    input_list_positive_divisor = [10, 20, 30]
    divisor_three = 3
    result_generator_three = divide_list(input_list_positive_divisor, divisor_three)
    results_three = list(result_generator_three)
    print(results_three)