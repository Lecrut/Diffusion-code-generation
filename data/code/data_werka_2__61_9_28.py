class ElementRetriever:
    ERROR_MESSAGE = "Index out of bounds"

    @staticmethod
    def is_valid_index(index, lst):
        return isinstance(index, int) and 0 <= index < len(lst)

    def __init__(self, data):
        self.data = data

    def get_element(self, index):
        if not self.is_valid_index(index, self.data):
            raise ValueError(self.ERROR_MESSAGE)
        return self.data[index]

if __name__ == '__main__':
    sample_list = [1000, 2000, 3000, 4000, 5000]
    index_to_retrieve = 2
    retriever = ElementRetriever(sample_list)
    try:
        element = retriever.get_element(index_to_retrieve)
        print(element)
    except ValueError as e:
        print(e)