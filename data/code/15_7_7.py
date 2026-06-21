def get_second_last_element(lst: list) -> any:
    if len(lst) < 2:
        raise ValueError("List must have at least two elements")
    return lst[-2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_second_last_element(sample_list)
    print(result)