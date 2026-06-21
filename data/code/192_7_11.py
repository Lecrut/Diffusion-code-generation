def common_elements(iterable1, iterable2):
    set2 = set(iterable2)
    for item in iterable1:
        if item in set2:
            yield item

if __name__ == '__main__':
    sample1 = [1, 2, 3, 4, 5]
    sample2 = [4, 5, 6, 7, 8]
    print(list(common_elements(sample1, sample2)))