class MiddleElementFinder:
    def find_middle_element(self, data):
        n = len(data)
        middle_index = n // 2
        if n % 2 == 0:
            return (data[middle_index - 1], data[middle_index])
        else:
            return data[middle_index]

if __name__ == '__main__':
    finder = MiddleElementFinder()
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [100]
    list4 = [5, 15, 25, 35, 45, 55]
    
    print(f"Middle element of {list1}: {finder.find_middle_element(list1)}")
    print(f"Middle element of {list2}: {finder.find_middle_element(list2)}")
    print(f"Middle element of {list3}: {finder.find_middle_element(list3)}")
    print(f"Middle element of {list4}: {finder.find_middle_element(list4)}")