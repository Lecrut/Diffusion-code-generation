def retrieve_third_element(data_list):
    target_index = 2
    list_length = len(data_list)
    if list_length > target_index:
        return data_list[target_index]
    return None

if __name__ == '__main__':
    hardcoded_integers = [5, 15, 25, 35, 45, 55]
    extracted_value = retrieve_third_element(hardcoded_integers)
    print(extracted_value)