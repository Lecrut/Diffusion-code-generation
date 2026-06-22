class ListRetriever:
    def __init__(self, data):
        self.data = data

    def get_last_item(self):
        if not self.data:
            raise IndexError("List is empty")
        return self.data[-1]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    retriever = ListRetriever(sample_data)
    result = retriever.get_last_item()
    print(result)