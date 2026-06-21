def get_last_element(data):
    return data[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_last_element(sample_list))
    print(get_last_element(['apple', 'banana', 'cherry']))
    print(get_last_element([True, False, True]))