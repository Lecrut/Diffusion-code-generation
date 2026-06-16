def compare_pairs(seq1, seq2):
    for a in seq1:
        for b in seq2:
            yield (a, b)
if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    results = list(compare_pairs(list1, list2))
    for pair in results:
        print(pair)