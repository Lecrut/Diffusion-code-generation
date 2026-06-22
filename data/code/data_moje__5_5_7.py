def compare_lengths(seq_a, seq_b):
    is_iter_a = hasattr(seq_a, '__iter__') and (not isinstance(seq_a, (str, bytes)))
    is_iter_b = hasattr(seq_b, '__iter__') and (not isinstance(seq_b, (str, bytes)))
    if not is_iter_a:
        len_a = len(seq_a)
    else:
        len_a = sum((1 for _ in seq_a))
    if not is_iter_b:
        len_b = len(seq_b)
    else:
        len_b = sum((1 for _ in seq_b))
    yield (len_a > len_b)
if __name__ == '__main__':
    result_a = list(compare_lengths([1, 2, 3], [1, 2]))
    print(result_a)
    result_b = list(compare_lengths('hello', 'hi'))
    print(result_b)
    result_c = list(compare_lengths((x for x in range(5)), (x for x in range(10))))
    print(result_c)
    result_d = list(compare_lengths([1, 2], [3, 4]))
    print(result_d)