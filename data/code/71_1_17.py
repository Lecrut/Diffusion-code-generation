class ListProcessor:
    def find_middle_element(self, data):
        n = len(data)
        middle_index = (n - 1) // 2
        return data[middle_index]

if __name__ == '__main__':
    processor = ListProcessor()
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [100]
    list4 = [5, 15, 25, 35]

    print(processor.find_middle_element(list1))
    print(processor.find_middle_element(list2))
    print(processor.find_middle_element(list3))
    print(processor.find_middle_element(list4))