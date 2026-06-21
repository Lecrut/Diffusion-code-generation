from typing import List, Dict

def validate_input(elements: List) -> None:
    if not isinstance(elements, list):
        raise TypeError("Input must be a list")
    for element in elements:
        if not isinstance(element, (int, str)):
            raise ValueError("List elements must be integers or strings")

def count_elements(elements: List) -> Dict:
    validate_input(elements)
    element_count = {}
    for element in elements:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    return element_count

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    result = count_elements(sample_list)
    print(result)