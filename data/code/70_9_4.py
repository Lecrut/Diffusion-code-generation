class ListChecker:
    def __init__(self, data):
        self.data = data

    def get_first_and_last(self):
        if not self.data:
            raise ValueError("List is empty")
        first = self.data[0]
        last = self.data[-1]
        return first, last

if __name__ == '__main__':
    checker = ListChecker([10, 20, 30, 40, 50])
    result = checker.get_first_and_last()
    print(result)