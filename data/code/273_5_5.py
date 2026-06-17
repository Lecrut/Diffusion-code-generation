def repeat_iterable(iterable, n):
    if n <= 0:
        return
    for _ in range(n):
        yield from iterable
if __name__ == '__main__':
    my_list = [1, 2]
    n_repeats = 3
    result_generator = repeat_iterable(my_list, n_repeats)
    result_list = list(result_generator)
    print(result_list)
    my_string = ['a', 'b']
    n_repeats_str = 2
    result_generator_str = repeat_iterable(my_string, n_repeats_str)
    result_list_str = list(result_generator_str)
    print(result_list_str)