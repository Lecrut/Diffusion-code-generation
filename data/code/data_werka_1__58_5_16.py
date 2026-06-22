def validate_input(input_iterable):
    if not isinstance(input_iterable, list):
        raise ValueError("Input must be a list")
    if len(input_iterable) == 0:
        return False
    return True

def first_element_generator(input_list):
    if not validate_input(input_list):
        return
    yield input_list[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    generator = first_element_generator(sample_list)
    result = next(generator)
    print(result)

    sample_list_empty = []
    try:
        generator_empty = first_element_generator(sample_list_empty)
        print(next(generator_empty))
    except StopIteration:
        print("Generator for empty list yielded nothing")