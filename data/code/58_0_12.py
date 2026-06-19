class ListHandler:
    def __init__(self, elements):
        self.elements = elements

    def get_first_element(self):
        if not self.elements:
            return None
        return self.elements[0]

    def display_first_element(self):
        first_element = self.get_first_element()
        print(f"The first element is: {first_element}")

if __name__ == '__main__':
    sample_list = [9, 18, 27, 36]
    handler = ListHandler(sample_list)
    handler.display_first_element()