class ListRetriever:
    def get_last_item(self, lst):
        if not lst:
            return None
        return lst[-1]

if __name__ == '__main__':
    retriever = ListRetriever()
    sample_list = [1, 2, 3, 4, 5]
    result = retriever.get_last_item(sample_list)
    print(result)