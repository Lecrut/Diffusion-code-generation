def get_last_element(data):
    if not data:
        raise IndexError("list index out of range")
    return data[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_element(sample_list)
    print(result)