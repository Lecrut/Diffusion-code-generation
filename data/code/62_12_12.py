class ListElementRetriever:
    def __init__(self, data):
        self._data = list(data)
    
    def get_second(self):
        if len(self._data) < 2:
            raise IndexError("List does not have a second element")
        return self._data[1]

if __name__ == '__main__':
    my_list = [10, 20, 30, 40]
    retriever = ListElementRetriever(my_list)
    try:
        second_element = retriever.get_second()
        print(second_element)
    except IndexError as e:
        print(e)

    short_list = [5, 6]
    short_retriever = ListElementRetriever(short_list)
    try:
        print(short_retriever.get_second())
    except IndexError as e:
        print(e)

    single_element_list = [7]
    single_retriever = ListElementRetriever(single_element_list)
    try:
        print(single_retriever.get_second())
    except IndexError as e:
        print(e)