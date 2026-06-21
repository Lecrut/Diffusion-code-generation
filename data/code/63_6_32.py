class FastFirstElement:
    def __init__(self, elements):
        self._validate_input(elements)
        self.first_element = None if not elements else elements[0]
    
    def _validate_input(self, elements):
        if not isinstance(elements, list):
            raise ValueError("Input must be a list")
    
    def get_first_element(self):
        return self.first_element

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28]
    first_finder = FastFirstElement(sample_list)
    print(first_finder.get_first_element())