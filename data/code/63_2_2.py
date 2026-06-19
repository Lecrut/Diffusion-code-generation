class ElementRetriever:
    def __init__(self, elements):
        self.elements = elements

    def get_first(self):
        return self.elements[0]

if __name__ == '__main__':
    sample_values = {'list1': [5, 10, 15], 'list2': [25, 30, 35]}
    retriever = ElementRetriever(sample_values['list1'])
    print(retriever.get_first())