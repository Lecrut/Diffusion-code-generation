class ElementRetriever:
    def __init__(self, collection):
        self._collection = collection

    def retrieve_first(self):
        if not self._collection:
            return None
        return self._collection[0]

if __name__ == '__main__':
    sample_list = [1024, 2048, 4096, 8192]
    retriever = ElementRetriever(sample_list)
    first_element = retriever.retrieve_first()
    print(first_element)