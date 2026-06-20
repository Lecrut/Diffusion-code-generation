def compare_lengths_generator(seq1, seq2):
    iterator1 = iter(seq1)
    iterator2 = iter(seq2)
    while True:
        try:
            item1 = next(iterator1)
        except StopIteration:
            break
        try:
            item2 = next(iterator2)
        except StopIteration:
            break
        len1 = len(item1)
        len2 = len(item2)
        if len1 < len2:
            yield (-1)
        elif len1 > len2:
            yield 1
        else:
            yield 0
if __name__ == '__main__':
    list1 = ['apple', 'banana', 'cherry', 'date']
    list2 = ['fig', 'grape', 'honeydew', 'kiwi']
    results = list(compare_lengths_generator(list1, list2))
    print(results)