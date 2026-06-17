def count_generator(data):
    count = 0
    for item in data:
        yield count
        count += 1
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result_generator = count_generator(sample_list)
    result_list = list(result_generator)
    print(result_list)