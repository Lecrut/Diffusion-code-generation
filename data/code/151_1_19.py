def concatenate_lists(list_a, list_b):
    if not all(isinstance(item, str) for item in list_a + list_b):
        raise ValueError("Both lists must contain only strings.")
    return [item for sublist in (list_a, list_b) for item in sublist]

if __name__ == '__main__':
    list_a = ["apple", "banana", "cherry"]
    list_b = ["date", "elderberry", "fig"]
    result = concatenate_lists(list_a, list_b)
    print(result)