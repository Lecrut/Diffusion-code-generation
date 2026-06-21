def filter_elements(input_list, element_to_filter):
    return [element for element in input_list if element != element_to_filter]

if __name__ == '__main__':
    sample_input = [10, 20, 30, 40, 50, 60]
    value_to_filter = 30
    filtered_output = filter_elements(sample_input, value_to_filter)
    print(f"Original List: {sample_input}")
    print(f"Value to Filter: {value_to_filter}")
    print(f"Filtered List: {filtered_output}")