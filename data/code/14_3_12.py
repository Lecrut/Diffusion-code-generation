def third_element(iterable):
    iterator = iter(iterable)
    for i in range(3):
        try:
            result = next(iterator)
        except StopIteration:
            return None
    return result

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(third_element(sample_list))
    sample_tuple = ('a', 'b', 'c')
    print(third_element(sample_tuple))
    sample_short = [1, 2]
    print(third_element(sample_short))
    sample_generator = (x * x for x in range(10))
    print(third_element(sample_generator))