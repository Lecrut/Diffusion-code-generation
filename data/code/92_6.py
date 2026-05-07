def opposite_generator(iterable):
    for value in iterable:
        yield not value
if __name__ == '__main__':
    sample_data = [True, False, True, False, True]
    result_generator = opposite_generator(sample_data)
    result_list = list(result_generator)
    print(result_list)