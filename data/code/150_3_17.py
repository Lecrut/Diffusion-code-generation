def find_index(lst, target):
    try:
        return lst.index(target)
    except ValueError:
        return None

def remove_integer(lst, target):
    index = find_index(lst, target)
    if index is not None:
        lst.pop(index)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    integer_to_remove = 30
    remove_integer(sample_list, integer_to_remove)
    print(sample_list)