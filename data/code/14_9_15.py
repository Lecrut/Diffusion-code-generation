def safe_extract_third_element(data, default=None):
    if len(data) >= 3:
        return data[2]
    return default

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40]
    sample_list_2 = [1, 2]
    sample_list_3 = []
    result_1 = safe_extract_third_element(sample_list_1, default="Missing")
    result_2 = safe_extract_third_element(sample_list_2, default="Missing")
    result_3 = safe_extract_third_element(sample_list_3, default="Missing")
    print(result_1)
    print(result_2)
    print(result_3)