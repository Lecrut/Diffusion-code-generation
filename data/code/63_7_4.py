def find_first_element_o1(data_list):
    if not data_list:
        raise IndexError("List is empty")
    return data_list[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = find_first_element_o1(sample_list)
    print(result)
    sample_list_empty = []
    try:
        result_empty = find_first_element_o1(sample_list_empty)
        print(result_empty)
    except IndexError as e:
        print(f"Error: {e}")