class ListHandler:
    def __init__(self, elements):
        self.elements = elements

    def print_elements(self):
        for index in range(len(self.elements)):
            print(self.elements[index])

    def get_element_count(self):
        return len(self.elements)

if __name__ == '__main__':
    sample_values = [50, 60, 70, 80, 90]
    handler = ListHandler(sample_values)
    handler.print_elements()
    print(f"Number of elements: {handler.get_element_count()}")