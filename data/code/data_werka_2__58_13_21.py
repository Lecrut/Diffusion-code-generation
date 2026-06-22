class ElementRetriever:
    def __init__(self, collection):
        self.collection = collection

    def get_first(self):
        if not self.collection:
            return None
        return self.collection[0]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    retriever = ElementRetriever(sample_data)
    first_element = retriever.get_first()
    print(first_element)

    empty_data = []
    empty_retriever = ElementRetriever(empty_data)
    first_empty_element = empty_retriever.get_first()
    print(first_empty_element)