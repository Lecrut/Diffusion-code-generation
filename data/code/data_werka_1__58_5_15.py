def first_element_generator(input_list):
    if input_list:
        yield input_list[0]

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40]
    empty_sample = []

    gen_with_elements = first_element_generator(sample_values)
    try:
        print(next(gen_with_elements))
    except StopIteration:
        print("No elements to yield")

    gen_empty = first_element_generator(empty_sample)
    try:
        print(next(gen_empty))
    except StopIteration:
        print("Generator for empty list yielded nothing")