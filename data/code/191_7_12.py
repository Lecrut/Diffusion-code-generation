def merge_lists(list_x, list_y):
    return list_x + list_y

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = ['a', 'b', 'c']
    combined = merge_lists(list_a, list_b)
    print(combined)