def divide_list(data, divisor):
    for number in data:
        if divisor != 0:
            yield number / divisor
if __name__ == '__main__':
    input_list = [10, 20, 30, 40, 50]
    divisor = 5
    result_generator = divide_list(input_list, divisor)
    output_list = list(result_generator)
    print(output_list)
    input_list_with_zero = [10, 20, 0, 40, 50]
    divisor_zero = 0
    result_generator_zero = divide_list(input_list_with_zero, divisor_zero)
    output_list_zero = list(result_generator_zero)
    print(output_list_zero)