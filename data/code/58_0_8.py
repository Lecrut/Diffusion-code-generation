class FirstElementAccessor:
    def __init__(self, elements):
        self.elements = elements

    def get_first(self):
        if not self.elements:
            raise ValueError("The list is empty.")
        return self.elements[0]

if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry']
    accessor = FirstElementAccessor(sample_data)
    first_item = accessor.get_first()
    print(first_item)