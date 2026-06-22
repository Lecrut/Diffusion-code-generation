def yield_first_element(iterable):
    if iterable:
        first = next(iter(iterable), None)
        yield first

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    generator = yield_first_element(sample_list)
    print(next(generator))
    
    empty_list = []
    empty_generator = yield_first_element(empty_list)
    try:
        print(next(empty_generator))
    except StopIteration:
        print("No elements yielded from the empty list")