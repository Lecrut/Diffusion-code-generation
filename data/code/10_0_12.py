class NumberListHandler:
    def __init__(self, data):
        self.data = data

    def get_first(self):
        return self.data[0]

    def get_count(self):
        return len(self.data)

numbers = [42, 99, 7, 13, 5]
handler = NumberListHandler(numbers)
if __name__ == '__main__':
    print(handler.get_first())
    print(handler.get_count())