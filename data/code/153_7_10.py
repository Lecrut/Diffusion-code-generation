def item_exists_in_nested_list(nested_list, target):

    def flatten(lst):
        for el in lst:
            if isinstance(el, list):
                yield from flatten(el)
            else:
                yield el
    return target in set(flatten(nested_list))
if __name__ == '__main__':
    sample_list = [1, 2, [3, 4, [5]], 6]
    print(item_exists_in_nested_list(sample_list, 5))
    print(item_exists_in_nested_list(sample_list, 7))