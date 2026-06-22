class LastElementRetriever:
    def __init__(self, collection):
        self.collection = collection

    def retrieve(self):
        if len(self.collection) == 0:
            raise IndexError("Cannot retrieve from an empty collection")
        return self.collection[-1]

if __name__ == '__main__':
    test_list = [5, 12, 7, 9, 100]
    test_tuple = (1, 3, 5, 7, 9, 11)
    test_str = "algorithm"
    
    list_retriever = LastElementRetriever(test_list)
    tuple_retriever = LastElementRetriever(test_tuple)
    str_retriever = LastElementRetriever(test_str)
    
    print(list_retriever.retrieve())
    print(tuple_retriever.retrieve())
    print(str_retriever.retrieve())