def extract_every_second_element(input_list):
    return [input_list[i] for i in range(1, len(input_list), 2)]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    result = extract_every_second_element(sample_list)
    print(result)