def find_smallest(generator):
    smallest = None
    for value in generator:
        if smallest is None or value < smallest:
            smallest = value
    return smallest

if __name__ == '__main__':
    sample_generator = (x * x for x in range(10000))
    print(find_smallest(sample_generator))