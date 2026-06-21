def exclude_element(source_list, element_to_exclude):
    return [element for element in source_list if element != element_to_exclude]

if __name__ == '__main__':
    initial_list = [7, 8, 9, 10, 8, 11]
    target_element = 8
    modified_list = exclude_element(initial_list, target_element)
    print(f"Initial list: {initial_list}")
    print(f"Target element to exclude: {target_element}")
    print(f"Modified list: {modified_list}")