def common_elements(iterable1, iterable2):
    set2 = set(iterable2)
    for element in iterable1:
        if element in set2:
            yield element

if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    sample2 = [4, 5, 6, 7, 8]
    print(list(common_elements(sample1, sample2)))