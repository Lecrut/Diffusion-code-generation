def concatenate_lists(list_a, list_b):
    return [item for item in list_a + list_b]

if __name__ == '__main__':
    list_a = ["apple", "banana"]
    list_b = ["cherry", "date"]
    result = concatenate_lists(list_a, list_b)
    print(result)