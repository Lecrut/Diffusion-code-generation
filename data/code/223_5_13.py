def find_max_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    max_value = data[0]
    for element in data[1:]:
        if element > max_value:
            max_value = element
    
    return max_value

if __name__ == '__main__':
    sample_list1 = [3.14, 2.718, 1.618, 4.0]
    sample_list2 = [-5.5, -1.2, -8.9, -3.3]
    sample_list3 = [100.0, 50.0, 150.0, 75.0]
    sample_list4 = [0.0, -1.0, 0.0]
    
    print(f"Max of {sample_list1}: {find_max_element(sample_list1)}")
    print(f"Max of {sample_list2}: {find_max_element(sample_list2)}")
    print(f"Max of {sample_list3}: {find_max_element(sample_list3)}")
    print(f"Max of {sample_list4}: {find_max_element(sample_list4)}")