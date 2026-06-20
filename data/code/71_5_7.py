def middle_element_generator(iterable):
    iterator = iter(iterable)
    first_half = []
    second_half = []
    try:
        while True:
            first_half.append(next(iterator))
            if len(first_half) > len(second_half) + 1:
                second_half.insert(0, first_half.pop())
            elif len(first_half) == len(second_half) + 2:
                yield second_half[0]
                second_half = [first_half.pop()]
    except StopIteration:
        if first_half and (not second_half):
            yield first_half[0]
        elif second_half:
            yield second_half[0]
if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    gen = middle_element_generator(sample_values)
    print(next(gen))