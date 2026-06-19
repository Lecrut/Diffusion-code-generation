def first_element_generator(input_iterable):
    for item in input_iterable:
        yield item
        break

if __name__ == '__main__':
    sample_values = [42, 84, 168]
    generator_result = first_element_generator(sample_values)
    try:
        first_element = next(generator_result)
        print(first_element)
    except StopIteration:
        print("The iterable is empty")