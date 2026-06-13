def combine_lists(list_x, list_y):
    result = []
    for item in list_x:
        result.append(item)
    for item in list_y:
        result.append(item)
    return result
if __name__ == '__main__':
    list_x_sample = [1, 2, 3]
    list_y_sample = ['a', 'b', 'c']
    combined = combine_lists(list_x_sample, list_y_sample)
    print(combined)