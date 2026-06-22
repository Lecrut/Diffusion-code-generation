class ListRetriever:
    def __init__(self, data):
        self._data = data

    def fetch_first(self):
        if not self._data:
            return None
        return self._data[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    retriever = ListRetriever(sample_list)
    first_element = retriever.fetch_first()
    print(first_element)