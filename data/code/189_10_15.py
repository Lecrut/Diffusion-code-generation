def remove_element(lst, element):
    result = []
    for item in lst:
        if item != element:
            result.append(item)
    return result

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10, 8, 11]
    element_to_remove = 8
    modified_list = remove_element(sample_list, element_to_remove)
    print(modified_list)