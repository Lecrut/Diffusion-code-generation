def remove_element(lst, element):
    result = []
    for item in lst:
        if item != element:
            result.append(item)
    return result

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45, 25, 55]
    element_to_remove = 25
    modified_list = remove_element(sample_list, element_to_remove)
    print(modified_list)