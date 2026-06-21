from typing import List, Dict

def count_elements(elements: List) -> Dict:
    element_count = {}
    for element in elements:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    return element_count

if __name__ == '__main__':
    sample_list = [4, 5, 6, 7, 8, 9, 4, 5]
    result = count_elements(sample_list)
    print(result)