def get_first_element(data):
    return data[0]

if __name__ == '__main__':
    sample_list1 = [42, 84, 168]
    sample_list2 = ['apple', 'banana', 'cherry']
    
    try:
        first_element1 = get_first_element(sample_list1)
        print(f"The first element of {sample_list1} is: {first_element1}")
        
        first_element2 = get_first_element(sample_list2)
        print(f"The first element of {sample_list2} is: {first_element2}")
    except IndexError as e:
        print(f"Error: The list is empty. {e}")