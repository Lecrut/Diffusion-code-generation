from typing import List, Dict

class ElementCounter:
    def __init__(self, data: List):
        self._data = data
    
    def count_elements(self) -> Dict:
        element_count = {}
        for element in self._data:
            if element in element_count:
                element_count[element] += 1
            else:
                element_count[element] = 1
        return element_count

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    counter = ElementCounter(sample_list)
    result = counter.count_elements()
    print(result)