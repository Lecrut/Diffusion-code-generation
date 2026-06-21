def remove_integer(lst, target):
    try:
        index = lst.index(target)
        lst.pop(index)
    except ValueError:
        return

if __name__ == '__main__':
    sample_list = [5, 3, 8, 2, 9, 1]
    integer_to_remove = 8
    remove_integer(sample_list, integer_to_remove)
    print(sample_list)