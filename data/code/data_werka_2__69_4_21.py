def extract_every_second_element(input_list):
    return [element for index, element in enumerate(input_list) if (index + 1) % 2 == 0]
if __name__ == '__main__':
    sample_list = [True, 'hello', 3.14, 42, 'world', 7, False]
    extracted_elements = extract_every_second_element(sample_list)
    print(extracted_elements)