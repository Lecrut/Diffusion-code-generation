class ListProcessor:
    @staticmethod
    def find_middle_element(data):
        n = len(data)
        middle_index = n // 2
        return data[middle_index]

if __name__ == '__main__':
    processor = ListProcessor()
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    list3 = [7]
    list4 = [100, 200, 300, 400, 500, 600]
    print(processor.find_middle_element(list1))
    print(processor.find_middle_element(list2))
    print(processor.find_middle_element(list3))
    print(processor.find_middle_element(list4))