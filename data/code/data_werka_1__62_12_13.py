class ListElementRetriever:
    def __init__(self, data):
        self.data = data

    def get_second_element(self):
        if len(self.data) > 1:
            return self.data[1]
        return None

if __name__ == '__main__':
    my_list = [10, 20, 30, 40]
    retriever = ListElementRetriever(my_list)
    second_element = retriever.get_second_element()
    print(second_element)

    short_list = [5, 15]
    short_retriever = ListElementRetriever(short_list)
    second_short = short_retriever.get_second_element()
    print(second_short)

    single_element_list = [7]
    single_retriever = ListElementRetriever(single_element_list)
    second_single = single_retriever.get_second_element()
    print(second_single)