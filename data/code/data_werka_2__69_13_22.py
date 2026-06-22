def fetch_elements(elements):
    if not elements:
        return ()
    
    first_element = elements[0]
    last_element = elements[-1]
    middle_index = len(elements) // 2
    middle_element = elements[middle_index]
    
    return (first_element, last_element, middle_element)

if __name__ == '__main__':
    test_list = [7, 14, 21, 28, 35, 42]
    output = fetch_elements(test_list)
    print(output)