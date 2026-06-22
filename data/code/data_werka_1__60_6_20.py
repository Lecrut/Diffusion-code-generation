class SafeListRetriever:
    def __init__(self, data):
        self.data = data

    def get_last_element(self):
        try:
            return self.data[-1]
        except IndexError:
            return None

if __name__ == '__main__':
    sample_data_1 = [1, 2, 3, 4, 5]
    retriever_1 = SafeListRetriever(sample_data_1)
    print(retriever_1.get_last_element())

    sample_data_2 = []
    retriever_2 = SafeListRetriever(sample_data_2)
    print(retriever_2.get_last_element())

    sample_data_3 = ['a', 'b', 'c']
    retriever_3 = SafeListRetriever(sample_data_3)
    print(retriever_3.get_last_element())