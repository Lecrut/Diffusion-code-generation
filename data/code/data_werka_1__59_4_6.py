class MiddleElementFinder:
    @staticmethod
    def find_middle_element(lst):
        n = len(lst)
        middle_index = n // 2
        return lst[middle_index]

if __name__ == '__main__':
    sample_list = [5.5, 6.6, 7.7, 8.8, 9.9]
    print(MiddleElementFinder.find_middle_element(sample_list))