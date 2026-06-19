def first_element_generator(input_list):
    def validate_input(lst):
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")
        if len(lst) == 0:
            return False
        return True

    if validate_input(input_list):
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