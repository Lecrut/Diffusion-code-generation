class ListChecker:
    def __init__(self, data):
        self.data = data

    def check_ends(self):
        if len(self.data) < 2:
            raise ValueError("List must contain at least two elements")
        return (self.data[0], self.data[-1])

if __name__ == '__main__':
    checker = ListChecker([1, 2, 3, 4, 5])
    result = checker.check_ends()
    print(result)