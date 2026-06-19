def retrieve_first_item(data_list):
    if not data_list:
        raise IndexError("The list is empty and has no first item.")
    return data_list[0]

if __name__ == '__main__':
    sample_list1 = [5, 15, 25]
    sample_list2 = []
    
    try:
        print(retrieve_first_item(sample_list1))
    except IndexError as e:
        print(f"Error with sample_list1: {e}")
    
    try:
        print(retrieve_first_item(sample_list2))
    except IndexError as e:
        print(f"Error with sample_list2: {e}")