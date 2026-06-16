def divide_list(data, divisor):
    for item in data:
        if divisor != 0:
            yield item / divisor
if __name__ == '__main__':
    input_list = [10, 20, 30, 40, 50]
    divisor = 5
    result_generator = divide_list(input_list, divisor)
    results = list(result_generator)
    print(results)