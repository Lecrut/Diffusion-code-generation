def concatenate_string_lists(list1, list2):
    return list1 + list2
if __name__ == '__main__':
    list_a = ["hello", "world"]
    list_b = ["python", "programming"]
    result = concatenate_string_lists(list_a, list_b)
    print(result)