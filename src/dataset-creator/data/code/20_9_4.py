def filter_values(iterable, condition):
    for item in iterable:
        if condition(item):
            yield item
if __name__ == '__main__':
    sample_data = [10, -5, 20, -3.5, 40]
    def is_non_negative(value):
        return value >= 0
    result_list = list(filter_values(sample_data, is_non_negative))
    print(result_list)