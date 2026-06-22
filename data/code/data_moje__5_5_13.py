def compare_lengths_generator(seq1, seq2):
    len1 = len(seq1)
    len2 = len(seq2)
    if len1 < len2:
        yield -1
    elif len1 > len2:
        yield 1
    else:
        yield 0

if __name__ == '__main__':
    data_a = [1, 2, 3, 4, 5]
    data_b = [10, 20, 30]
    data_c = [100, 200, 300, 400, 500]
    print(list(compare_lengths_generator(data_a, data_b)))
    print(list(compare_lengths_generator(data_a, data_c)))
    print(list(compare_lengths_generator(data_b, data_c)))