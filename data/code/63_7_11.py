class ElementFinder:
    def __init__(self, data_list):
        self.data_list = data_list

    def find_first_element(self):
        if not self.data_list:
            raise IndexError("List is empty")
        return self.data_list[0]

if __name__ == '__main__':
    list1 = [10, 20, 30, 40, 50]
    list2 = [99, 1, 5, 1000]
    list3 = [42]
    list4 = []

    finder1 = ElementFinder(list1)
    print(f"List 1: {list1}, First element: {finder1.find_first_element()}")

    finder2 = ElementFinder(list2)
    print(f"List 2: {list2}, First element: {finder2.find_first_element()}")

    finder3 = ElementFinder(list3)
    print(f"List 3: {list3}, First element: {finder3.find_first_element()}")

    try:
        finder4 = ElementFinder(list4)
        print(f"List 4: {list4}, First element: {finder4.find_first_element()}")
    except IndexError as e:
        print(f"List 4: {list4}, Error: {e}")