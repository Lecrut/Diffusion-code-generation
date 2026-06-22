class ListRetriever:
    def __init__(self, data):
        self.data = data

    def retrieve_first(self):
        if not self.data:
            return None
        return self.data[0]

if __name__ == '__main__':
    sample_values = [5, 15, 25, 35]
    retriever = ListRetriever(sample_values)
    first_element = retriever.retrieve_first()
    print(first_element)