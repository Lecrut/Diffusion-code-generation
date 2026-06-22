def find_middle_element(lst):
    if not lst:
        raise ValueError('The list is empty')
    MIDDLE_INDEX = len(lst) // 2
    return lst[MIDDLE_INDEX]

class MiddleElementFinder:
    def __init__(self, data):
        self.data = data
    def get_middle(self):
        return find_middle_element(self.data)

if __name__ == '__main__':
    SAMPLE_ODD_LIST = [7, 14, 21, 28, 35]
    SAMPLE_EVEN_LIST = [10, 20, 30, 40, 50, 60]
    
    finder_odd = MiddleElementFinder(SAMPLE_ODD_LIST)
    finder_even = MiddleElementFinder(SAMPLE_EVEN_LIST)
    
    print(finder_odd.get_middle())
    print(finder_even.get_middle())