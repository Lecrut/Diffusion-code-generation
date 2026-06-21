def retrieve_elements(numbers):
    if not numbers:
        return ()
    
    FIRST_INDEX = 0
    LAST_INDEX = -1
    MIDDLE_INDEX = len(numbers) // 2
    
    first_element = numbers[FIRST_INDEX]
    last_element = numbers[LAST_INDEX]
    middle_element = numbers[MIDDLE_INDEX]
    
    return (first_element, last_element, middle_element)

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    result = retrieve_elements(sample_list)
    print(result)