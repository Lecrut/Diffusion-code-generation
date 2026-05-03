def get_first_element(input_list):
    if not input_list:
        return
    yield input_list[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    generator = get_first_element(sample_list)
    result = list(generator)
    print(result)
    sample_list_empty = []
    generator_empty = get_first_element(sample_list_empty)
    result_empty = list(generator_empty)
    print(result_empty)