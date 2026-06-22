class MiddleElementFinder:
    @staticmethod
    def find_middle_element(lst):
        if not lst:
            raise ValueError('The list is empty')
        middle_index = len(lst) // 2
        return lst[middle_index]

if __name__ == '__main__':
    sample_odd_list = [1, 3, 5, 7, 9]
    sample_even_list = [2, 4, 6, 8, 10, 12]
    
    print(MiddleElementFinder.find_middle_element(sample_odd_list))
    print(MiddleElementFinder.find_middle_element(sample_even_list))