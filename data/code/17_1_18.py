class ListRetriever:
    def get_last_item(self, items):
        if not items:
            return None
        return items[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    retriever = ListRetriever()
    result = retriever.get_last_item(sample_list)
    print(result)