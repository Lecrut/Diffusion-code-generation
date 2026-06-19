def first_element_generator(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    if len(input_list) == 0:
        return
    yield input_list[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    generator = first_element_generator(sample_list)
    try:
        result = next(generator)
        print(result)
    except StopIteration:
        print("Generator for empty list yielded nothing")

    sample_list_empty = []
    generator_empty = first_element_generator(sample_list_empty)
    try:
        next(generator_empty)
    except StopIteration:
        print("Generator for empty list yielded nothing")