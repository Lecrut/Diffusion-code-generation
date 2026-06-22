def get_last_element(data):
    result = data[-1:]
    return result[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_last_element(sample_list))