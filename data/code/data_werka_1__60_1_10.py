def get_last_item(data):
    return data[-1] if data else None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    last_element = get_last_item(sample_list)
    print(f"The last element of {sample_list} is: {last_element}")

    empty_list = []
    last_element_empty = get_last_item(empty_list)
    print(f"The last element of {empty_list} is: {last_element_empty}")