def validate_input(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError('Input must be an iterable')

def check_endpoints(iterable):
    validate_input(iterable)
    try:
        first = next(iter(iterable))
        last = iterable[-1]
        return (first, last)
    except StopIteration:
        return (None, None)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(check_endpoints(sample_list))
    empty_list = []
    print(check_endpoints(empty_list))
    sample_string = 'hello'
    print(check_endpoints(sample_string))
    single_element = [42]
    print(check_endpoints(single_element))