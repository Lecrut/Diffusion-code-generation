class ListMiddleFinder:
    def __init__(self, data):
        self.data = data

    def get_middle(self):
        n = len(self.data)
        if n == 0:
            return None
        middle_index = n // 2
        return self.data[middle_index]

if __name__ == '__main__':
    finder1 = ListMiddleFinder([1, 2, 3, 4, 5])
    print(finder1.get_middle())

    finder2 = ListMiddleFinder([10, 20, 30])
    print(finder2.get_middle())

    finder3 = ListMiddleFinder([50])
    print(finder3.get_middle())

    finder4 = ListMiddleFinder([])
    print(finder4.get_middle())