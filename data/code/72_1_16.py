def compare_elements_at_index(first_list, second_list, target_index):
    FIRST_LIST_LABEL = "first"
    SECOND_LIST_LABEL = "second"
    EQUALITY_LABEL = "equal"
    
    first_element = first_list[target_index]
    second_element = second_list[target_index]
    
    if first_element > second_element:
        return (FIRST_LIST_LABEL, first_element, SECOND_LIST_LABEL, second_element)
    if first_element < second_element:
        return (SECOND_LIST_LABEL, second_element, FIRST_LIST_LABEL, first_element)
    return (EQUALITY_LABEL, first_element, EQUALITY_LABEL, second_element)

if __name__ == '__main__':
    data_a = [1, 42, 9, 16]
    data_b = [1, 42, 9, 16]
    position = 1
    outcome = compare_elements_at_index(data_a, data_b, position)
    print(outcome)
    
    data_c = [10, 20, 30]
    data_d = [10, 25, 30]
    position_2 = 1
    outcome_2 = compare_elements_at_index(data_c, data_d, position_2)
    print(outcome_2)