def extract_every_second_element(input_list):
    return [input_list[i] for i in range(1, len(input_list), 2)]

if __name__ == '__main__':
    sample_list = [0, 'a', 2, 'b', 4, 'c', 6, 'd']
    result = extract_every_second_element(sample_list)
    print(result)