class ListRetriever:
    def __init__(self, data):
        self.data = data

    def get_last_item(self):
        return self.data[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    retriever = ListRetriever(sample_list)
    result = retriever.get_last_item()
    print(result)