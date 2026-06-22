def get_first_element(numbers):
    if len(numbers) == 0:
        return None
    return numbers[0]

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20]
    result = get_first_element(sample_list)
    print(result)
    empty_list = []
    result_empty = get_first_element(empty_list)
    print(result_empty)