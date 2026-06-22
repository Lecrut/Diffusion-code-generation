def get_special_elements(numbers):
    if not numbers:
        return ()
    
    FIRST_INDEX = 0
    LAST_INDEX = -1
    
    first_element = numbers[FIRST_INDEX]
    last_element = numbers[LAST_INDEX]
    middle_index = len(numbers) // 2
    middle_element = numbers[middle_index]
    
    return (first_element, last_element, middle_element)

if __name__ == '__main__':
    sample_list = [3, 6, 9, 12, 15, 18, 21]
    result = get_special_elements(sample_list)
    print(result)