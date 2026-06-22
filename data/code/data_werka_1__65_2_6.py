class ElementRetriever:
    def __init__(self, data):
        self.data = data

    def get_third(self):
        if len(self.data) < 3:
            raise IndexError("List does not have a third element")
        return self.data[2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    retriever = ElementRetriever(sample_list)
    try:
        third_element = retriever.get_third()
        print(third_element)
    except IndexError as e:
        print(e)