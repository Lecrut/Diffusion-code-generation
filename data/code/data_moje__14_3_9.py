def third_element(iterable):
    it = iter(iterable)
    for _ in range(3):
        try:
            item = next(it)
        except StopIteration:
            return None
    return item

if __name__ == '__main__':
    sample_iterable = [10, 20, 30, 40, 50]
    print(third_element(sample_iterable))
    sample_tuple = ('a', 'b', 'c', 'd')
    print(third_element(sample_tuple))
    sample_short = [1, 2]
    print(third_element(sample_short))
    sample_generator = (x * 2 for x in range(5))
    print(third_element(sample_generator))