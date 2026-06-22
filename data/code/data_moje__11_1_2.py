def safe_pop_last(items):
    try:
        return items.pop()
    except IndexError:
        return None

if __name__ == '__main__':
    test_list = [10, 20, 30]
    result = safe_pop_last(test_list)
    print(result)
    print(test_list)
    empty_list = []
    result_empty = safe_pop_last(empty_list)
    print(result_empty)
    print(empty_list)