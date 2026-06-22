class MiddleElementFinder:
    FLOOR_OFFSET = 1

    @staticmethod
    def _validate_input(lst):
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")
        if len(lst) == 0:
            raise ValueError("List must not be empty")

    @staticmethod
    def find_middle_element(lst):
        MiddleElementFinder._validate_input(lst)
        n = len(lst)
        index = (n - MiddleElementFinder.FLOOR_OFFSET) // 2
        return lst[index]

if __name__ == '__main__':
    odd_list = [11, 22, 33, 44, 55]
    even_list = [11, 22, 33, 44]
    
    print(MiddleElementFinder.find_middle_element(odd_list))
    print(MiddleElementFinder.find_middle_element(even_list))