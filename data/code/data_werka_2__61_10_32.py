class ElementRetriever:
    def __init__(self, data):
        self.data = data

    def get_element_at_position(self, index):
        if not isinstance(index, int) or index < 0 or index >= len(self.data):
            raise ValueError('Index is out of bounds')
        return self.data[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    retriever = ElementRetriever(sample_list)
    try:
        print(retriever.get_element_at_position(2))
        print(retriever.get_element_at_position(5))
    except ValueError as e:
        print(e)