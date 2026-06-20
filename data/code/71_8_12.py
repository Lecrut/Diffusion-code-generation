class ListManager:

    def __init__(self, data):
        self.data = data

    def find_middle(self):
        n = len(self.data)
        if n == 0:
            return None
        middle_index = n // 2
        if n % 2 == 1:
            return self.data[middle_index]
        else:
            return (self.data[middle_index - 1], self.data[middle_index])
if __name__ == '__main__':
    list_manager1 = ListManager([1, 2, 3, 4, 5])
    print(list_manager1.find_middle())
    list_manager2 = ListManager([10, 20, 30])
    print(list_manager2.find_middle())
    list_manager3 = ListManager([50])
    print(list_manager3.find_middle())
    list_manager4 = ListManager([])
    print(list_manager4.find_middle())
    list_manager5 = ListManager([1, 2, 3, 4])
    print(list_manager5.find_middle())
    list_manager6 = ListManager([100, 200])
    print(list_manager6.find_middle())