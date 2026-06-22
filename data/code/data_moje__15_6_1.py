def get_penultimate_element(data):
    length = len(data)
    index = length - 2
    return data[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_penultimate_element(sample_list)
    print(result)