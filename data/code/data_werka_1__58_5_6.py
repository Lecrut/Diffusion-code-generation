def first_element_generator(input_list):
    if not input_list:
        return
    yield input_list[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    generator = first_element_generator(sample_list)
    try:
        print(next(generator))
    except StopIteration:
        print("No elements in the list")

    empty_list = []
    empty_generator = first_element_generator(empty_list)
    try:
        print(next(empty_generator))
    except StopIteration:
        print("Generator for empty list yielded nothing")