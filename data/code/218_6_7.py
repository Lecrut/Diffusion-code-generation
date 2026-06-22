def find_minimum(data: list) -> float:
    if not data:
        raise ValueError("The input list is empty")
    
    current_min = float('inf')
    
    for element in data:
        if element < current_min:
            current_min = element
    
    return current_min

if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3]
    print(find_minimum(sample_list))