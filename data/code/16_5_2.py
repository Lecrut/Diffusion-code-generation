def positive_generator(input_iterable):
    for x in input_iterable:
        if x > 0:
            yield True
if __name__ == '__main__':
    sample_data = [-2, 0, 5, -1, 10, 0.5]
    result_generator = positive_generator(sample_data)
    result_list = list(result_generator)
    print(result_list)