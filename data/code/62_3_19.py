class ElementRetriever:
    def __init__(self, elements):
        self._elements = elements

    @classmethod
    def get_second_element(cls, instance):
        if len(instance._elements) < 2:
            return None
        return instance._elements[1]

if __name__ == '__main__':
    sample_data = [7, 14, 21, 28]
    retriever = ElementRetriever(sample_data)
    print(ElementRetriever.get_second_element(retriever))
    
    short_data = [3]
    short_retriever = ElementRetriever(short_data)
    print(ElementRetriever.get_second_element(short_retriever))