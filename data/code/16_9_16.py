def get_first_element(numbers):
    if len(numbers) == 0:
        return None
    first_item = numbers[0]
    return first_item

if __name__ == '__main__':
    data_set = [55, 67, 89]
    empty_set = []
    result_full = get_first_element(data_set)
    result_empty = get_first_element(empty_set)
    print(result_full)
    print(result_empty)