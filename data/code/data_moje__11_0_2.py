def get_last_element(data):
    length = len(data)
    index = -length
    return data[index]

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    last_item = get_last_element(sample_values)
    print(last_item)