def find_first_element_o1(data_list):
    if not data_list:
        raise IndexError("List is empty")
    return data_list[0]

if __name__ == '__main__':
    list_a = [7, 8, 9, 10]
    list_b = [42]
    list_c = []
    
    try:
        print(find_first_element_o1(list_a))
    except IndexError as e:
        print(f"Error for list_a: {e}")
    
    try:
        print(find_first_element_o1(list_b))
    except IndexError as e:
        print(f"Error for list_b: {e}")
    
    try:
        print(find_first_element_o1(list_c))
    except IndexError as e:
        print(f"Error for list_c: {e}")