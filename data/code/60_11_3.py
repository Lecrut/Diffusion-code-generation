class ListRetriever:
    def __init__(self, items):
        self.items = items

    def get_last(self):
        if not self.items:
            raise IndexError("Cannot retrieve last element from an empty list")
        return self.items[-1]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    retriever = ListRetriever(sample_list)
    print(retriever.get_last())