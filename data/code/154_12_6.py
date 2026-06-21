from typing import List, Dict

def validate_input(elements: List) -> bool:
    return isinstance(elements, list)

def count_elements(elements: List) -> Dict:
    if not validate_input(elements):
        raise ValueError("Input must be a list")
    
    element_count = {}
    for element in elements:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    return element_count

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    print(count_elements(sample_list))