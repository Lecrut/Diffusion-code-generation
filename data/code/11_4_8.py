def get_last_element(data):
    return data[len(data) - 1]

if __name__ == '__main__':
    sample_list = [10, 25, 42, 88, 103]
    result = get_last_element(sample_list)
    print(result)