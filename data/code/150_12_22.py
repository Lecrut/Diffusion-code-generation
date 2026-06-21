def remove_item(lst, target):
    if isinstance(target, int) and 0 <= target < len(lst):
        return lst[:target] + lst[target + 1:]
    elif target in lst:
        index = lst.index(target)
        return lst[:index] + lst[index + 1:]
    else:
        raise ValueError('Target not found in list')
if __name__ == '__main__':
    sample_list = ['red', 'green', 'blue', 'yellow']
    print(remove_item(sample_list, 2))
    print(remove_item(sample_list, 'green'))
    try:
        print(remove_item(sample_list, 'purple'))
    except ValueError as e:
        print(e)