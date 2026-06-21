class SortedList:
    def __init__(self, data):
        self.data = sorted(data)

    def find_middle(self):
        n = len(self.data)
        if n == 0:
            raise ValueError("The list is empty")
        middle_index = n // 2
        return self.data[middle_index]

if __name__ == '__main__':
    sample_list1 = SortedList([1, 5, 2, 8, 3])
    print(sample_list1.find_middle())

    sample_list2 = SortedList([10, 20, 30, 40, 50, 60])
    print(sample_list2.find_middle())

    sample_list3 = SortedList([7])
    print(sample_list3.find_middle())

    sample_list4 = SortedList([100, 200])
    print(sample_list4.find_middle())