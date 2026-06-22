def min_nested_list(nested):
    def flatten(lst):
        for elem in lst:
            if isinstance(elem, list):
                yield from flatten(elem)
            else:
                yield elem

    return min(flatten(nested))

if __name__ == '__main__':
    sample = [[1, 2, [3]], 4, [5, 6], 7]
    print(min_nested_list(sample))