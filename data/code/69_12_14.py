def access_list_elements():
    sample_data = [10, 20, 30, 40, 50]
    positive_index = 2
    negative_index = -1
    
    element_positive = sample_data[positive_index]
    element_negative = sample_data[negative_index]
    
    return element_positive, element_negative

if __name__ == '__main__':
    positive_element, negative_element = access_list_elements()
    print(f"Element at positive index 2: {positive_element}")
    print(f"Element at negative index -1: {negative_element}")