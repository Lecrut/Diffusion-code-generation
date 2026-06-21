def extract_every_second_element(input_list):
    return [input_list[i] for i in range(1, len(input_list), 2)]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60, 70]
    result = extract_every_second_element(sample_list)
    print(result)