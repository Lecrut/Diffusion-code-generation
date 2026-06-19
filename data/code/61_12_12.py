class SafeElementRetriever:

    def __init__(self, data_list):
        self.data_list = data_list

    @classmethod
    def fetch_element(cls, instance, index):
        if 0 <= index < len(instance.data_list):
            return instance.data_list[index]
        return None
if __name__ == '__main__':
    sample_elements = ['apple', 'banana', 'cherry', 'date']
    retriever = SafeElementRetriever(sample_elements)
    print(SafeElementRetriever.fetch_element(retriever, 1))
    print(SafeElementRetriever.fetch_element(retriever, -1))
    print(SafeElementRetriever.fetch_element(retriever, 4))
    print(SafeElementRetriever.fetch_element(retriever, 2))