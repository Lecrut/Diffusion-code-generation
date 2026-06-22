def first_element_generator(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    if not input_list:
        return
    yield input_list[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    try:
        generator = first_element_generator(sample_list)
        result = next(generator)
        print(result)
    except TypeError as e:
        print(e)

    sample_list_empty = []
    try:
        generator_empty = first_element_generator(sample_list_empty)
        result_empty = next(generator_empty)
        print(result_empty)
    except StopIteration:
        print("Generator for empty list yielded nothing")
    except TypeError as e:
        print(e)

    invalid_input = "not a list"
    try:
        generator_invalid = first_element_generator(invalid_input)
        next(generator_invalid)
    except TypeError as e:
        print(e)