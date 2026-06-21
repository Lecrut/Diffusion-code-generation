def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    largest = data[0]
    for number in data[1:]:
        if number > largest:
            largest = number
    
    return largest

if __name__ == '__main__':
    try:
        sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
        print(f"List: {sample_list}, Largest element: {find_largest(sample_list)}")
        
        negative_list = [-10, -5, -20, -1]
        print(f"List: {negative_list}, Largest element: {find_largest(negative_list)}")
        
        single_element_list = [7]
        print(f"List: {single_element_list}, Largest element: {find_largest(single_element_list)}")
        
        empty_list = []
        print(f"List: {empty_list}, Largest element: {find_largest(empty_list)}")
    except ValueError as e:
        print(e)