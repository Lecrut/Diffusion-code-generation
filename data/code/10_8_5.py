def extract_first_element(data):
    return data[:1]

if __name__ == '__main__':
    sample_list = [42, "hello", 3.14, True]
    result = extract_first_element(sample_list)
    print(result)