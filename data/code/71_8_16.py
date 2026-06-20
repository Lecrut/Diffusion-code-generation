class ListWithMiddle:

    def __init__(self, data):
        self.data = data

    def get_middle(self):
        n = len(self.data)
        if n == 0:
            return None
        middle_index = n // 2
        return self.data[middle_index]
if __name__ == '__main__':
    list1 = ListWithMiddle([1, 2, 3, 4, 5])
    print(list1.get_middle())
    list2 = ListWithMiddle([10, 20, 30])
    print(list2.get_middle())
    list3 = ListWithMiddle([50])
    print(list3.get_middle())
    list4 = ListWithMiddle([])
    print(list4.get_middle())