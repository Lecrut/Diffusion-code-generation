def subtract_fixed_value(data, fixed_value):
    for item in data:
        yield item - fixed_value
if __name__ == '__main__':
    input_list = [10, 20, 30, 40, 50]
    fixed_subtractor = 5
    result_generator = subtract_fixed_value(input_list, fixed_subtractor)
    output_list = list(result_generator)
    print(output_list)