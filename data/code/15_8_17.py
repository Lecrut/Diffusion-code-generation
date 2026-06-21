def get_element_before_last(data):
    if len(data) < 2:
        raise IndexError("List must contain at least two elements")
    return data[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_element_before_last(sample_list)
    print(result)