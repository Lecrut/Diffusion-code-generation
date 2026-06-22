def get_second_last_element(numbers):
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
    return numbers[-2]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_second_last_element(sample_data)
    print(result)
    empty_list = [1]
    try:
        get_second_last_element(empty_list)
    except ValueError as e:
        print(e)