def flatten_and_find_largest(data):
    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item

    if not data:
        return None

    return max(flatten(data))

if __name__ == '__main__':
    sample_list = [12, 45, [67, 89], 34, [91, [5]]]
    result = flatten_and_find_largest(sample_list)
    print(result)