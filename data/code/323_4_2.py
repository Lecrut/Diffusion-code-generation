def subtract_from_fixed(data, fixed_value):
    for element in data:
        yield fixed_value - element
if __name__ == '__main__':
    input_list = [10, 25, 30, 45]
    fixed_number = 50
    result_generator = subtract_from_fixed(input_list, fixed_number)
    results = list(result_generator)
    print(results)