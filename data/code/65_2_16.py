class ElementRetriever:
    def __init__(self, data):
        self._data = data

    def retrieve(self, index):
        return self._data[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    retriever = ElementRetriever(sample_list)
    print(retriever.retrieve(2))