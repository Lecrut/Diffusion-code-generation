class ListRetriever:
    def __init__(self, data):
        self.data = data

    def get_last_item(self):
        if not self.data:
            raise IndexError("Cannot retrieve the last item from an empty list.")
        return self.data[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    retriever = ListRetriever(sample_list)
    print(retriever.get_last_item())
    empty_list = []
    empty_retriever = ListRetriever(empty_list)
    try:
        print(empty_retriever.get_last_item())
    except IndexError as e:
        print(e)