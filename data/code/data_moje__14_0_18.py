class ThirdElementRetriever:
    def __init__(self, data):
        self.data = data

    def get_third(self):
        if len(self.data) < 3:
            raise IndexError("List has fewer than three items")
        return self.data[2]

if __name__ == '__main__':
    valid_data = [10, 25, 42, 99, 150]
    invalid_data = [7, 33]

    valid_retriever = ThirdElementRetriever(valid_data)
    print(valid_retriever.get_third())

    invalid_retriever = ThirdElementRetriever(invalid_data)
    try:
        print(invalid_retriever.get_third())
    except IndexError as error:
        print(error)