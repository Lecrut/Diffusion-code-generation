class MiddleFinder:
    def __init__(self, data):
        self.data = sorted(data)

    def find_middle(self):
        middle_index = len(self.data) // 2
        return self.data[middle_index]

if __name__ == '__main__':
    list1 = [5, 3, 8, 1, 4]
    list2 = [10, 20, 30, 40, 50, 60]
    list3 = [99, 100]
    list4 = [1, 2, 3, 4, 5, 6, 7]

    finder1 = MiddleFinder(list1)
    finder2 = MiddleFinder(list2)
    finder3 = MiddleFinder(list3)
    finder4 = MiddleFinder(list4)

    print(finder1.find_middle())
    print(finder2.find_middle())
    print(finder3.find_middle())
    print(finder4.find_middle())