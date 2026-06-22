class IndexFinder:
    def __init__(self, data):
        self.data = data

    def find_last_index(self, value):
        last_index = -1
        for i in range(len(self.data) - 1, -1, -1):
            if self.data[i] == value:
                last_index = i
                break
        return last_index

if __name__ == '__main__':
    list1 = [1, 5, 2, 5, 8, 5]
    finder1 = IndexFinder(list1)
    value1 = 5
    result1 = finder1.find_last_index(value1)
    print(f"List: {list1}, Value: {value1}, Last Index: {result1}")

    list2 = [10, 20, 30, 20, 40]
    finder2 = IndexFinder(list2)
    value2 = 20
    result2 = finder2.find_last_index(value2)
    print(f"List: {list2}, Value: {value2}, Last Index: {result2}")

    list3 = [1, 2, 3, 4, 5]
    finder3 = IndexFinder(list3)
    value3 = 99
    result3 = finder3.find_last_index(value3)
    print(f"List: {list3}, Value: {value3}, Last Index: {result3}")