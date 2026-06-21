def remove_element(lst, element):
    result = []
    for item in lst:
        if item != element:
            result.append(item)
    return result

if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3, 4, 2, 5]
    ELEMENT_TO_REMOVE = 2
    MODIFIED_LIST = remove_element(SAMPLE_LIST, ELEMENT_TO_REMOVE)
    print(MODIFIED_LIST)