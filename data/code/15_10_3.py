def get_penultimate_element(input_list):
    if not input_list:
        raise ValueError("List is empty")
    return input_list[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_penultimate_element(sample_list)
    print(result)
    empty_list = []
    try:
        get_penultimate_element(empty_list)
    except ValueError as e:
        print(f"Error: {e}")