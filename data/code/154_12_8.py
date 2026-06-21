from typing import List, Dict

def count_elements(elements: List) -> Dict:
    element_count = {}
    for element in elements:
        element_count[element] = element_count.get(element, 0) + 1
    return element_count

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c', 'a', 'b', 'c', 'd']
    result = count_elements(sample_list)
    print(result)