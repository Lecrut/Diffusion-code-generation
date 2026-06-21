def remove_integer(lst, target):
    try:
        index = lst.index(target)
        lst.pop(index)
    except ValueError:
        return

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20, 25]
    integer_to_remove = 15
    remove_integer(sample_list, integer_to_remove)
    print(sample_list)