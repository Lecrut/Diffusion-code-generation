def element_generator(input_iterable):
    for element in input_iterable:
        yield element
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print("Starting generator execution:")
    generator = element_generator(sample_list)
    for item in generator:
        print(item)