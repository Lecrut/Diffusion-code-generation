class ListRetriever:
    def __init__(self, data):
        self.data = data

    def get_element(self, index):
        try:
            return self.data[index]
        except IndexError:
            raise ValueError("Index out of bounds")

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    index_to_retrieve = 2
    retriever = ListRetriever(sample_list)
    try:
        element = retriever.get_element(index_to_retrieve)
        print(element)
    except ValueError as e:
        print(e)