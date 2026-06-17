def repeat_iterable(iterable, n):
    if n <= 0:
        return
    for _ in range(n):
        yield from iterable
if __name__ == '__main__':
    sample_iterable = [1, 2]
    n_repeats = 3
    result_generator = repeat_iterable(sample_iterable, n_repeats)
    result_list = list(result_generator)
    print(result_list)