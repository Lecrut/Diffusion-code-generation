def first_element_generator(input_list):
    def validate_input():
        if not isinstance(input_list, list):
            raise ValueError("Input must be a list")
        if not input_list:
            return False
        return True

    if validate_input():
        yield input_list[0]

if __name__ == '__main__':
    sample_list = [50, 60, 70, 80]
    generator = first_element_generator(sample_list)
    result = next(generator)
    print(result)

    sample_list_empty = []
    generator_empty = first_element_generator(sample_list_empty)
    try:
        next(generator_empty)
    except StopIteration:
        print("Generator for empty list yielded nothing")