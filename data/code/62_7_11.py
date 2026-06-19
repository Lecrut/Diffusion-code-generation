class ListElementFinder:
    def __init__(self, data):
        self.data = data

    def find_second_element(self, index=0):
        if len(self.data) < 2:
            raise IndexError("List has fewer than two elements")
        if index == 1:
            return self.data[1]
        return self.find_second_element(index + 1)

if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [5, 15]
    list3 = [7]
    list4 = [99]

    finder1 = ListElementFinder(list1)
    finder2 = ListElementFinder(list2)
    finder3 = ListElementFinder(list3)
    finder4 = ListElementFinder(list4)

    print(f"Second element of {list1}: {finder1.find_second_element()}")
    print(f"Second element of {list2}: {finder2.find_second_element()}")
    try:
        print(f"Second element of {list3}: {finder3.find_second_element()}")
    except IndexError as e:
        print(f"Error for {list3}: {e}")
    try:
        print(f"Second element of {list4}: {finder4.find_second_element()}")
    except IndexError as e:
        print(f"Error for {list4}: {e}")