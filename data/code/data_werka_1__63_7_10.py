def find_first_element_o1(data_list):
    if not data_list:
        raise IndexError("List is empty")
    return data_list[0]

if __name__ == '__main__':
    sample_list_1 = [5, 15, 25, 35, 45]
    sample_list_2 = [7, 17, 27]
    sample_list_3 = []
    
    try:
        first_element_1 = find_first_element_o1(sample_list_1)
        print(f"First element of {sample_list_1}: {first_element_1}")
    except IndexError as e:
        print(f"Error for {sample_list_1}: {e}")

    try:
        first_element_2 = find_first_element_o1(sample_list_2)
        print(f"First element of {sample_list_2}: {first_element_2}")
    except IndexError as e:
        print(f"Error for {sample_list_2}: {e}")

    try:
        first_element_3 = find_first_element_o1(sample_list_3)
        print(f"First element of {sample_list_3}: {first_element_3}")
    except IndexError as e:
        print(f"Error for {sample_list_3}: {e}")