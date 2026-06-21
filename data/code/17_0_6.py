def get_last_element(data):
    return data[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_last_element(sample_list))
    sample_string = "Hello"
    print(get_last_element(sample_string))
    sample_tuple = (1, 2, 3)
    print(get_last_element(sample_tuple))