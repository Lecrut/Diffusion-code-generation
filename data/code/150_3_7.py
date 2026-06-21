def find_index(lst, target):
    for i, item in enumerate(lst):
        if item == target:
            return i
    raise ValueError("Target not found in list")

def remove_integer(lst, target):
    try:
        index = find_index(lst, target)
        lst.pop(index)
    except ValueError:
        return

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    integer_to_remove = 30
    remove_integer(sample_list, integer_to_remove)
    print(sample_list)