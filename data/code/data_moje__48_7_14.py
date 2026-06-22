def find_max_in_nested(nested):
    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item
    return max(flatten(nested))

if __name__ == '__main__':
    sample = [1, [2, 3], [[4, 5], 6], [7, [8, [9, 10]]]]
    print(find_max_in_nested(sample))