def fetch_first_element(data):
    if not data:
        raise IndexError("The list is empty and does not contain any elements.")
    return data[0]

if __name__ == '__main__':
    sample_list_1 = [5, 15, 25]
    sample_list_2 = []
    
    try:
        first_element_1 = fetch_first_element(sample_list_1)
        print(f"The first element of sample_list_1 is: {first_element_1}")
    except IndexError as e:
        print(f"Error with sample_list_1: {e}")
    
    try:
        first_element_2 = fetch_first_element(sample_list_2)
        print(f"The first element of sample_list_2 is: {first_element_2}")
    except IndexError as e:
        print(f"Error with sample_list_2: {e}")