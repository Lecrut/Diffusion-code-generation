from typing import List, Dict

class ElementCounter:
    def __init__(self, elements: List):
        self._element_count = {}
        for element in elements:
            if element in self._element_count:
                self._element_count[element] += 1
            else:
                self._element_count[element] = 1
    
    def get_element_count(self) -> Dict:
        return self._element_count

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    counter = ElementCounter(sample_list)
    count_dict = counter.get_element_count()
    print(count_dict)