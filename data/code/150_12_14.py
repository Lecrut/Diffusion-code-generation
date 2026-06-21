def remove_item(lst, target):
    if isinstance(target, int) and 0 <= target < len(lst):
        return lst[:target] + lst[target + 1:]
    elif target in lst:
        index = lst.index(target)
        return lst[:index] + lst[index + 1:]
    else:
        return lst

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(remove_item(sample_list, 2))
    print(remove_item(sample_list, 30))
    print(remove_item(sample_list, 60))