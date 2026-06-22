def extract_first_element(lst):
    return lst[:1]

if __name__ == '__main__':
    sample_list = [42, "hello", 3.14, True, [1, 2, 3]]
    result = extract_first_element(sample_list)
    print(result)