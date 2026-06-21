def find_smallest(generator):
    try:
        smallest = next(generator)
        for value in generator:
            if value < smallest:
                smallest = value
        return smallest
    except StopIteration:
        return None

if __name__ == '__main__':
    sample_data = (x**2 for x in range(1000000))
    print(find_smallest(sample_data))