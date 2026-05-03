def first_element_generator(input_list):
    if not input_list:
        return
    yield input_list[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    generator = first_element_generator(sample_list)
    result = next(generator)
    print(result)
    sample_list_empty = []
    generator_empty = first_element_generator(sample_list_empty)
    try:
        next(generator_empty)
    except StopIteration:
        print("Generator for empty list yielded nothing")