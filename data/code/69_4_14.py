def extract_every_second_element(data_list):
    return data_list[1::2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60]
    result = extract_every_second_element(sample_list)
    print(result)