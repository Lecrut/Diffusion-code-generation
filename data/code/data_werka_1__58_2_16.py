def get_first_item(data_list):
    if not data_list:
        raise IndexError("The list is empty")
    return data_list[0]

if __name__ == '__main__':
    sample_list1 = [5, 15, 25]
    sample_list2 = []
    
    try:
        first_item1 = get_first_item(sample_list1)
        print(f"First item from sample_list1: {first_item1}")
    except IndexError as e:
        print(f"Error processing sample_list1: {e}")
    
    try:
        first_item2 = get_first_item(sample_list2)
        print(f"First item from sample_list2: {first_item2}")
    except IndexError as e:
        print(f"Error processing sample_list2: {e}")