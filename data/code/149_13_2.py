def reverse_generator(iterable):
    it = iter(iterable)
    try:
        last = next(it)
    except StopIteration:
        return
    while True:
        yield last
        try:
            last = next(it)
        except StopIteration:
            break
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(list(reverse_generator(sample_list)))
    sample_tuple = (10, 20, 30, 40)
    print(list(reverse_generator(sample_tuple)))
    sample_string = "ABCDE"
    print(list(reverse_generator(sample_string)))