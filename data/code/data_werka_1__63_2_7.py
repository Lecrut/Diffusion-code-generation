class FirstElementRetriever:
    def __init__(self, elements):
        if not isinstance(elements, list):
            raise TypeError("Input must be a list.")
        self.elements = elements

    def retrieve(self):
        if not self.elements:
            raise ValueError("The list is empty.")
        return self.elements[0]

if __name__ == '__main__':
    sample_list = [100, 200, 300]
    retriever = FirstElementRetriever(sample_list)
    print(retriever.retrieve())