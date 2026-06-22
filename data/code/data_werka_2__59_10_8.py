class ListAnalyzer:
    EMPTY_LIST_ERROR = "The list is empty"

    @staticmethod
    def find_middle_element(lst):
        if not lst:
            raise ValueError(ListAnalyzer.EMPTY_LIST_ERROR)
        middle_index = len(lst) // 2
        return lst[middle_index]

if __name__ == '__main__':
    sample_odd_list = [7, 14, 21, 28, 35]
    sample_even_list = [10, 20, 30, 40, 50, 60]
    print(ListAnalyzer.find_middle_element(sample_odd_list))
    print(ListAnalyzer.find_middle_element(sample_even_list))