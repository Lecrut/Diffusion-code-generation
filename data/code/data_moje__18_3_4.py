def get_center_element(data):
    if not data:
        raise ValueError("List cannot be empty")
    return data[len(data) // 2]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40, 50]
    sample_list_2 = [1, 2, 3, 4]
    sample_list_3 = [99]
    
    result_1 = get_center_element(sample_list_1)
    result_2 = get_center_element(sample_list_2)
    result_3 = get_center_element(sample_list_3)
    
    print(result_1)
    print(result_2)
    print(result_3)