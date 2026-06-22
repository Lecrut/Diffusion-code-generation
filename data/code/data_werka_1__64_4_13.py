class Finder:
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
    finder1 = Finder(list1)
    value1 = 5
    print(finder1.find_last_index(value1))
    
    list2 = [10, 20, 30, 20, 40]
    finder2 = Finder(list2)
    value2 = 20
    print(finder2.find_last_index(value2))
    
    list3 = [5, 5, 5, 5]
    finder3 = Finder(list3)
    value3 = 5
    print(finder3.find_last_index(value3))
    
    list4 = [1, 2, 3, 4]
    finder4 = Finder(list4)
    value4 = 99
    print(finder4.find_last_index(value4))