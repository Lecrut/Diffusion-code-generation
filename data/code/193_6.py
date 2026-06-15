def list_sum_generator(data):
    total = 0
    for item in data:
        total += item
        yield total
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    generator = list_sum_generator(sample_list)
    result_iterator = list(generator)
    print(result_iterator)