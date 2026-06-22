class MiddleElementFinder:
    def __init__(self, lst):
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")
        if len(lst) == 0:
            raise ValueError("List cannot be empty")
        self.lst = lst

    @staticmethod
    def calculate_middle_index(n):
        return n // 2

    def find_middle_element(self):
        middle_index = self.calculate_middle_index(len(self.lst))
        return self.lst[middle_index]

if __name__ == '__main__':
    sample_list = [3.1, 4.5, 6.7, 8.9, 10.2]
    finder = MiddleElementFinder(sample_list)
    print(finder.find_middle_element())