def find_smallest_in_generator(gen):
    try:
        smallest = next(gen)
    except StopIteration:
        return None
    for number in gen:
        if number < smallest:
            smallest = number
    return smallest
if __name__ == '__main__':
    data = (10, 5, 2, 8, 1)
    smallest = find_smallest_in_generator(data)
    print(smallest)