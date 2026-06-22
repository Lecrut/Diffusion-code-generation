class ListProcessor:
    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def from_string(cls, string_elements):
        return cls(string_elements.split())

    def get_first_element(self):
        if self.elements:
            return self.elements[0]
        return None

if __name__ == '__main__':
    sample_list_processor = ListProcessor(['apple', 'banana', 'cherry'])
    print(sample_list_processor.get_first_element())