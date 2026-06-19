class ListElementRetriever:
    def __init__(self, elements):
        self.elements = elements

    def get_second(self):
        if len(self.elements) > 1:
            return self.elements[1]
        return None

if __name__ == '__main__':
    my_list = [10, 20, 30, 40]
    retriever = ListElementRetriever(my_list)
    second_element = retriever.get_second()
    print(second_element)

    short_list = [5, 15]
    short_retriever = ListElementRetriever(short_list)
    print(short_retriever.get_second())

    single_element_list = [7]
    single_retriever = ListElementRetriever(single_element_list)
    print(single_retriever.get_second())