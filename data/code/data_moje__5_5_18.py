def compare_lengths_generator(seq1, seq2):
    it1 = iter(seq1)
    it2 = iter(seq2)
    len1 = 0
    len2 = 0
    exhausted1 = False
    exhausted2 = False
    while not exhausted1 or not exhausted2:
        if not exhausted1:
            try:
                next(it1)
                len1 += 1
            except StopIteration:
                exhausted1 = True
        if not exhausted2:
            try:
                next(it2)
                len2 += 1
            except StopIteration:
                exhausted2 = True
        if exhausted1 and exhausted2:
            if len1 < len2:
                yield (-1)
            elif len1 > len2:
                yield 1
            else:
                yield 0
        elif exhausted1:
            yield (-1)
        else:
            yield 1
    if len1 < len2:
        yield (-1)
    elif len1 > len2:
        yield 1
    else:
        yield 0
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8]
    list3 = [9, 10, 11, 12, 13]
    results1 = list(compare_lengths_generator(list1, list2))
    print(results1[-1])
    results2 = list(compare_lengths_generator(list1, list3))
    print(results2[-1])
    results3 = list(compare_lengths_generator(list2, list1))
    print(results3[-1])