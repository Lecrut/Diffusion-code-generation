def first_element_generator(iterable):
    if iterable:
        yield iterable[0]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4],
        ['apple', 'banana', 'cherry'],
        [],
        [True, False],
        [None, None, None]
    ]
    
    for i, lst in enumerate(sample_lists):
        generator = first_element_generator(lst)
        try:
            result = next(generator)
            print(f"First element of list {i+1}: {result}")
        except StopIteration:
            print(f"No elements to yield from list {i+1}")