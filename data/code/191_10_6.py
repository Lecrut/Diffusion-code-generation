INITIAL_LIST = [1, 2, 3]
EXTENDING_LIST = [4, 5, 6]

def combine_lists(base_list, extension):
    base_copy = base_list.copy()
    base_copy.extend(extension)
    return base_copy

if __name__ == '__main__':
    result = combine_lists(INITIAL_LIST, EXTENDING_LIST)
    print(result)