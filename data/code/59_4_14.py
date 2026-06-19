class MiddleElementFinder:
    def __init__(self, lst):
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")
        if len(lst) == 0:
            raise ValueError("List cannot be empty")
        self.lst = lst

    def find_middle_element(self):
        n = len(self.lst)
        middle_index = n // 2
        return self.lst[middle_index]

if __name__ == '__main__':
    sample_list1 = [3.1, 4.5, 6.7, 8.9, 10.1]
    finder1 = MiddleElementFinder(sample_list1)
    print(finder1.find_middle_element())

    sample_list2 = [3.1, 4.5, 6.7, 8.9, 10.2]
    finder2 = MiddleElementFinder(sample_list2)
    print(finder2.find_middle_element())