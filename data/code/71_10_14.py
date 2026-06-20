class ListProcessor:
    @staticmethod
    def find_middle_element(data):
        return data[len(data) // 2]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [100]
    list4 = [5, 15, 25, 35, 45, 55]
    
    print(f"Middle element of {list1}: {ListProcessor.find_middle_element(list1)}")
    print(f"Middle element of {list2}: {ListProcessor.find_middle_element(list2)}")
    print(f"Middle element of {list3}: {ListProcessor.find_middle_element(list3)}")
    print(f"Middle element of {list4}: {ListProcessor.find_middle_element(list4)}")