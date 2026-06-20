def compare_lengths_generator(seq1, seq2):
    len1 = len(seq1)
    len2 = len(seq2)
    if len1 > len2:
        yield "first"
    elif len1 < len2:
        yield "second"
    else:
        yield "equal"

if __name__ == "__main__":
    data_a = list(range(10))
    data_b = list(range(5))
    for result in compare_lengths_generator(data_a, data_b):
        print(result)
    data_c = list(range(5))
    data_d = list(range(5))
    for result in compare_lengths_generator(data_c, data_d):
        print(result)
    data_e = list(range(3))
    data_f = list(range(8))
    for result in compare_lengths_generator(data_e, data_f):
        print(result)