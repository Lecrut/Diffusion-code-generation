def get_edge_elements(input_list):
    if len(input_list) == 0:
        raise ValueError("Input must be non-empty")
    first_element = input_list[0]
    last_element = input_list[-1]
    return (first_element, last_element)

if __name__ == '__main__':
    sample_data = [7, 14, 21, 28, 35]
    result = get_edge_elements(sample_data)
    print(result)