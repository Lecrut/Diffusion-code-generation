from collections.abc import Iterable
def count_elements(iterable):
    if not isinstance(iterable, Iterable) and hasattr(iterable, '__len__'):
        return len(iterable)
    counter = 0
    for _ in iterable:
        counter += 1
    return counter
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_tuple = ('a', 'b')
    sample_string = "hello"
    print(count_elements(sample_list))
    print(count_elements(sample_tuple))
    print(count_elements(sample_string))