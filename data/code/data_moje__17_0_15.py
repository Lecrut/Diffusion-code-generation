def get_last_element(items: list) -> object:
    return items[-1]

if __name__ == '__main__':
    sample_list = [10, 25, 30, 42, 99]
    result = get_last_element(sample_list)
    print(result)
    sample_mixed = ['apple', 123, 3.14, True]
    result_mixed = get_last_element(sample_mixed)
    print(result_mixed)