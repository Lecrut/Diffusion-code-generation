def append_lists(list_a, list_b):
    for item in list_b:
        list_a.append(item)
    return list_a

if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    result = append_lists(list_a, list_b)
    print(result)