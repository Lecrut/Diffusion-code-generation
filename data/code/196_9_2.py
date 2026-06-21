def concatenate_lists(list_x, list_y):
    result = list_x[:]
    result[len(result):] = list_y
    return result

if __name__ == '__main__':
    list_x = list(range(10**6))
    list_y = list(range(10**6, 2 * 10**6))
    result = concatenate_lists(list_x, list_y)
    print(len(result))