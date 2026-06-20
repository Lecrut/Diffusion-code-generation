class ListMiddleFinder:
    def __init__(self, data):
        self.data = data

    def find_middle(self):
        n = len(self.data)
        if n == 0:
            raise ValueError("List is empty")
        middle_index = n // 2
        return self.data[middle_index]

if __name__ == '__main__':
    finder1 = ListMiddleFinder([1, 2, 3, 4, 5])
    print(finder1.find_middle())

    finder2 = ListMiddleFinder([10, 20, 30])
    print(finder2.find_middle())

    finder3 = ListMiddleFinder([50])
    print(finder3.find_middle())

    try:
        finder4 = ListMiddleFinder([])
        print(finder4.find_middle())
    except ValueError as e:
        print(e)