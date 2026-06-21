def concatenate_lists(list_a, list_b):
    return [item for sublist in (list_a, list_b) for item in sublist]

if __name__ == '__main__':
    list_a = ['a', 'b', 'c']
    list_b = ['d', 'e', 'f']
    result = concatenate_lists(list_a, list_b)
    print(result)