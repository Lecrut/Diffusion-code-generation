def subtract_from_fixed(input_list, fixed_value):
    for element in input_list:
        yield fixed_value - element
if __name__ == '__main__':
    data = [10, 25, 30, 5]
    constant = 40
    result_generator = subtract_from_fixed(data, constant)
    results = list(result_generator)
    print(results)