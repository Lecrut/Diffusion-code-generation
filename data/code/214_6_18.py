def find_smallest(generator):
    try:
        smallest = next(generator)
        for value in generator:
            if value < smallest:
                smallest = value
        return smallest
    except StopIteration:
        raise ValueError('Generator is empty') from None
if __name__ == '__main__':
    data_generator = iter([10, 5, 2, 8, 1])
    result = find_smallest(data_generator)
    print(result)