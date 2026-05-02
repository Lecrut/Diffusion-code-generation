def last_element_generator(iterable):
    it = iter(iterable)
    try:
        last_element = next(it)
    except StopIteration:
        return
    while True:
        try:
            last_element = next(it)
        except StopIteration:
            yield last_element
            return
        yield last_element
if __name__ == '__main__':
    sequence1 = [1, 2, 3, 4, 5]
    print("Sequence 1:")
    for element in last_element_generator(sequence1):
        print(element)
    sequence2 = [10]
    print("\nSequence 2:")
    for element in last_element_generator(sequence2):
        print(element)
    sequence3 = []
    print("\nSequence 3 (Empty):")
    for element in last_element_generator(sequence3):
        print(element)
    sequence4 = [99]
    print("\nSequence 4:")
    for element in last_element_generator(sequence4):
        print(element)