class ListChecker:
    def __init__(self, data):
        self.data = list(data)

    def check_first_and_last(self):
        if len(self.data) < 2:
            raise ValueError("List must contain at least two elements")
        return (self.data[0], self.data[-1])

if __name__ == '__main__':
    checker = ListChecker([10, 20, 30, 40])
    result = checker.check_first_and_last()
    print(result)