class ListRetriever:
    def __init__(self, items):
        self.items = items

    def get_last_item(self):
        if not self.items:
            return None
        return self.items[len(self.items) - 1]

if __name__ == '__main__':
    sample_data = [10, 25, 30, 45, 50]
    retriever = ListRetriever(sample_data)
    print(retriever.get_last_item())
    empty_list = []
    empty_retriever = ListRetriever(empty_list)
    print(empty_retriever.get_last_item())
    single_item = [99]
    single_retriever = ListRetriever(single_item)
    print(single_retriever.get_last_item())