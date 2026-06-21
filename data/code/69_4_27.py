def extract_every_second_element(input_list):
    return [input_list[i] for i in range(len(input_list)) if i % 2 == 0]

if __name__ == '__main__':
    sample_list = [1, 'hello', 3.14, True, None, 'world']
    result = extract_every_second_element(sample_list)
    print("Extracted elements:", result)