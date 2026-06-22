class ListRetriever:
    def __init__(self, items):
        self.items = items

    def get_last_item(self):
        if not self.items:
            return None
        return self.items[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    retriever = ListRetriever(sample_list)
    print(retriever.get_last_item())
    empty_list = []
    empty_retriever = ListRetriever(empty_list)
    print(empty_retriever.get_last_item())