def divide_list(numbers, divisor):
    for number in numbers:
        if divisor != 0:
            yield number / divisor
if __name__ == '__main__':
    input_list = [10, 20, 30, 5, 0, -15]
    fixed_divisor = 5
    result_generator = divide_list(input_list, fixed_divisor)
    results = list(result_generator)
    print(results)