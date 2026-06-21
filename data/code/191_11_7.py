def merge_lists(list_a, list_b):
    try:
        return [*list_a, *list_b]
    except TypeError as e:
        raise ValueError("Both arguments must be lists") from e

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    result = merge_lists(list_a, list_b)
    print(result)