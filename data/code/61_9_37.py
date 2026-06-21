class ListElementRetriever:
    def __init__(self, data):
        self.data = data

    def retrieve_element(self, index):
        if not isinstance(index, int) or index < 0 or index >= len(self.data):
            raise ValueError("Index out of bounds")
        return self.data[index]

if __name__ == '__main__':
    SAMPLE_LIST = [7, 14, 21, 28, 35]
    INDEX_TO_RETRIEVE = 2
    retriever = ListElementRetriever(SAMPLE_LIST)
    try:
        element = retriever.retrieve_element(INDEX_TO_RETRIEVE)
        print(element)
    except ValueError as e:
        print(e)