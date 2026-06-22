def extract_every_second_element(input_list):
    return input_list[1::2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = extract_every_second_element(sample_list)
    print(result)