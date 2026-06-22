def find_middle_element(lst):
    if not lst:
        raise ValueError('The list is empty')
    MIDDLE_INDEX = len(lst) // 2
    return lst[MIDDLE_INDEX]

class MiddleElementFinder:
    def __init__(self, data):
        self.data = data
    def find(self):
        return find_middle_element(self.data)

if __name__ == '__main__':
    SAMPLE_ODD_LIST = [7, 11, 13, 17, 19]
    SAMPLE_EVEN_LIST = [2, 4, 6, 8, 10, 12]
    
    finder_odd = MiddleElementFinder(SAMPLE_ODD_LIST)
    finder_even = MiddleElementFinder(SAMPLE_EVEN_LIST)
    
    print(finder_odd.find())
    print(finder_even.find())