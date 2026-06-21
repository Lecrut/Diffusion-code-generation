def extract_first_element(input_list):
    first_element = input_list[:1]
    print(first_element[0])

if __name__ == '__main__':
    sample_list = [42, "hello", 3.14, True, [1, 2]]
    extract_first_element(sample_list)