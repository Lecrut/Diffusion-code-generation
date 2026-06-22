class ListAnalyzer:
    DEFAULT_VALUE = None

    def __init__(self, lst):
        if not isinstance(lst, list):
            raise ValueError('Input must be a list')
        self.lst = lst

    @staticmethod
    def _get_first_element(lst):
        return lst[0] if lst else ListAnalyzer.DEFAULT_VALUE

    def find_first_value(self):
        return ListAnalyzer._get_first_element(self.lst)

if __name__ == '__main__':
    sample_list1 = [5, 15, 25]
    sample_list2 = []
    analyzer1 = ListAnalyzer(sample_list1)
    analyzer2 = ListAnalyzer(sample_list2)
    print(analyzer1.find_first_value())
    print(analyzer2.find_first_value())