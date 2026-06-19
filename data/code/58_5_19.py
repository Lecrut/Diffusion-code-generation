def first_element_generator(input_iterable):
    if input_iterable:
        yield input_iterable[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    generator = first_element_generator(sample_list)
    try:
        print(next(generator))
    except StopIteration:
        print("No elements yielded from the list")

    empty_list = []
    empty_generator = first_element_generator(empty_list)
    try:
        print(next(empty_generator))
    except StopIteration:
        print("No elements yielded from the empty list")