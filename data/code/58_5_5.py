def first_element_generator(input_list):
    if input_list:
        yield input_list[0]

if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry']
    generator_instance = first_element_generator(sample_data)
    try:
        first_item = next(generator_instance)
        print(first_item)
    except StopIteration:
        print("No elements in the list")

    empty_sample = []
    empty_generator = first_element_generator(empty_sample)
    try:
        next(empty_generator)
    except StopIteration:
        print("Generator for empty list yielded nothing")