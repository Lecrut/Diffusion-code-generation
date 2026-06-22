def find_first_element(data_list):
    if not data_list:
        raise IndexError("List is empty")
    return data_list[0]

if __name__ == '__main__':
    SAMPLE_LIST_1 = [1, 2, 3, 4, 5]
    SAMPLE_LIST_2 = [100, 200, 300]
    SAMPLE_LIST_3 = []
    
    try:
        print(f"First element of {SAMPLE_LIST_1}: {find_first_element(SAMPLE_LIST_1)}")
    except IndexError as e:
        print(f"Error for {SAMPLE_LIST_1}: {e}")
    
    try:
        print(f"First element of {SAMPLE_LIST_2}: {find_first_element(SAMPLE_LIST_2)}")
    except IndexError as e:
        print(f"Error for {SAMPLE_LIST_2}: {e}")
    
    try:
        print(f"First element of {SAMPLE_LIST_3}: {find_first_element(SAMPLE_LIST_3)}")
    except IndexError as e:
        print(f"Error for {SAMPLE_LIST_3}: {e}")