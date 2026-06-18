def is_max_greater_than_second_to_last(numbers):
    if len(numbers) < 2:
        return False
    
    max_value = numbers[0]
    
    # Find maximum value in list (excluding potential duplicates logic, 
    # but strictly looking for the highest value regardless of position)
    actual_max_index = -1
    for idx, val in enumerate(numbers):
        if val > max_value:
            max_value = val
            actual_max_index = idx
            
    second_to_last_element = numbers[-2]
    
    return max_value > second_to_last_element

if __name__ == '__main__':
    pass
