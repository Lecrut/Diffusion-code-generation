class ListElementRetriever:
    OUT_OF_BOUNDS_MESSAGE = "Index out of bounds"

    def __init__(self, data):
        self.data = data

    def get_element(self, index):
        try:
            return self.data[index]
        except IndexError:
            raise ValueError(self.OUT_OF_BOUNDS_MESSAGE)

if __name__ == '__main__':
    sample_list = [50, 60, 70, 80, 90]
    index_to_retrieve = 2
    retriever = ListElementRetriever(sample_list)
    try:
        element = retriever.get_element(index_to_retrieve)
        print(element)
    except ValueError as e:
        print(e)