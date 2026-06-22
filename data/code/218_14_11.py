def min_nested_list(nested_list):
    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item

    return min(flatten(nested_list))

if __name__ == '__main__':
    sample = [1, [2, 3], [4, [5, 6]], 7]
    print(min_nested_list(sample))