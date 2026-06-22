class ListElementRetriever:
    def __init__(self, lst):
        self.lst = lst

    def get_second_element(self):
        if len(self.lst) < 2:
            raise IndexError("List does not contain at least two elements.")
        return self.lst[1]

if __name__ == '__main__':
    my_list = [10, 20, 30, 40]
    retriever = ListElementRetriever(my_list)
    print(retriever.get_second_element())