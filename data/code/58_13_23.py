class ElementRetriever:
    def __init__(self, data):
        self.data = data

    def get_first(self):
        if not self.data:
            return None
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28]
    retriever = ElementRetriever(sample_list)
    first_element = retriever.get_first()
    print(first_element)
    print(retriever.is_empty())
    
    empty_list = []
    empty_retriever = ElementRetriever(empty_list)
    print(empty_retriever.get_first())
    print(empty_retriever.is_empty())