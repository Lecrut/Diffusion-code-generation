class ElementRetriever:

    def __init__(self, elements):
        self._elements = elements

    def get_by_position(self, position):
        try:
            return self._elements[position]
        except IndexError:
            return None
if __name__ == '__main__':
    sample_elements = {'first': 10, 'second': 20, 'third': 30, 'fourth': 40, 'fifth': 50}
    retriever = ElementRetriever(list(sample_elements.values()))
    print(retriever.get_by_position(0))
    print(retriever.get_by_position(2))
    print(retriever.get_by_position(4))
    print(retriever.get_by_position(5))