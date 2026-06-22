class FastElementRetriever:
    def __init__(self, elements):
        if not isinstance(elements, list):
            raise ValueError("Input must be a list")
        self.first_element = None
        self._initialize_first_element(elements)

    def _initialize_first_element(self, elements):
        if elements:
            self.first_element = elements[0]

    def get_first_element(self):
        return self.first_element

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28, 35]
    retriever = FastElementRetriever(sample_list)
    print(retriever.get_first_element())