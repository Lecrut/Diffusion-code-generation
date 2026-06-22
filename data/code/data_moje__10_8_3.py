def extract_first_element(data_list):
    return data_list[:1][0]

if __name__ == '__main__':
    sample_list = [42, "hello", 3.14, True, None]
    result = extract_first_element(sample_list)
    print(result)