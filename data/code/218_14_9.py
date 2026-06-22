def min_nested_list(nested):
    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item

    return min(flatten(nested))

if __name__ == '__main__':
    sample = [3, [1, 2], [4, [5, 6]], 7]
    print(min_nested_list(sample))