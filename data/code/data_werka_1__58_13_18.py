class ListRetriever:
    def __init__(self, elements):
        self.elements = elements

    def fetch_first(self):
        if not self.elements:
            return None
        return self.elements[0]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400]
    retriever = ListRetriever(sample_list)
    first_element = retriever.fetch_first()
    print(first_element)

    empty_list = []
    empty_retriever = ListRetriever(empty_list)
    first_empty = empty_retriever.fetch_first()
    print(first_empty)