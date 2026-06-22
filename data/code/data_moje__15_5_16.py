class SecondToLastRetriever:
    def __init__(self, sequence):
        self.sequence = sequence

    def get(self):
        return self.sequence[-2]

    def get_index(self):
        return -2

if __name__ == '__main__':
    data = [5, 10, 15, 20, 25]
    retriever = SecondToLastRetriever(data)
    print(retriever.get())
    print(retriever.get_index())