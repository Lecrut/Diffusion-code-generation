class ElementRetriever:
    def __init__(self, data):
        self.data = data

    def retrieve_element(self, index):
        try:
            return self.data[index]
        except IndexError:
            raise ValueError("Index out of bounds")

if __name__ == '__main__':
    sample_list = [1000, 2000, 3000, 4000, 5000]
    index_to_retrieve = 2
    retriever = ElementRetriever(sample_list)
    try:
        element = retriever.retrieve_element(index_to_retrieve)
        print(element)
    except ValueError as e:
        print(e)