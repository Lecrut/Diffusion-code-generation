def find_smallest(generator):
    try:
        smallest = next(generator)
        for number in generator:
            if number < smallest:
                smallest = number
        return smallest
    except StopIteration:
        return None
if __name__ == '__main__':
    sample_data = (10, 5, 2, 8, 1)
    result = find_smallest(iter(sample_data))
    print(result)