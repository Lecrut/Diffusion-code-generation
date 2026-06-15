def process_set(integer_set):
    return [x for x in integer_set if x % 2 == 0]
if __name__ == '__main__':
    sample_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    result_list = process_set(sample_set)
    print(result_list)