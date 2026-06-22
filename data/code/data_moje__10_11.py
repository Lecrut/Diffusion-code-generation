def get_first_item(array):
    if len(array) == 0:
        return None
    return array[0]

if __name__ == '__main__':
    sample_array = [10, 20, 30]
    result = get_first_item(sample_array)
    print(result)
    empty_array = []
    empty_result = get_first_item(empty_array)
    print(empty_result)