def extract_tuple_element(t, index):
    if index < 0:
        return None
    if index >= len(t):
        return None
    return t[index]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    result = extract_tuple_element(sample_tuple, 2)
    print(result)
    result_out_of_bounds = extract_tuple_element(sample_tuple, 10)
    print(result_out_of_bounds)