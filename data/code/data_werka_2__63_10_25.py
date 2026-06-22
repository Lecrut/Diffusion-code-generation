class FirstElementRetriever:
    def __init__(self, lst):
        self.lst = lst

    def get_first_element(self):
        return self.lst[0]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35]
    retriever = FirstElementRetriever(sample_list)
    print(retriever.get_first_element())