def is_list_empty(items):
    return len(items) == 0

def get_last_element(items):
    if is_list_empty(items):
        return None
    last_index = len(items) - 1
    return items[last_index]

if __name__ == '__main__':
    sample_values = [5, 15, 25, 35]
    print(get_last_element(sample_values))
    print(get_last_element([]))
    print(get_last_element([42]))