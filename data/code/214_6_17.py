def find_smallest(generator):
    try:
        smallest = next(generator)
        for num in generator:
            if num < smallest:
                smallest = num
        return smallest
    except StopIteration:
        return None

if __name__ == '__main__':
    data_generator = (x for x in [10, 5, 2, 8, 1])
    result = find_smallest(data_generator)
    print(result)