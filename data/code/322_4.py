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
    input_list_zero_divisor = [10, 20, 0, 40, 50]
    divisor_zero = 0
    result_generator_zero = divide_list(input_list_zero_divisor, divisor_zero)
    results_zero = list(result_generator_zero)
    print(results_zero)