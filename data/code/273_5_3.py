def repeat_iterable(iterable, n):
    if n <= 0:
        return
    for _ in range(n):
        yield from iterable
if __name__ == '__main__':
    my_list = [1, 2]
    repeat_count = 3
    result_generator = repeat_iterable(my_list, repeat_count)
    result_list = list(result_generator)
    print(result_list)
    my_tuple = ('a', 'b')
    repeat_count = 2
    result_generator = repeat_iterable(my_tuple, repeat_count)
    result_list = list(result_generator)
    print(result_list)