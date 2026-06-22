class ListAnalyzer:

    def __init__(self, lst):
        if not isinstance(lst, list):
            raise ValueError('Input must be a list')
        self.lst = lst

    def find_first_value(self):
        return self.lst[0] if self.lst else None
if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = []
    analyzer1 = ListAnalyzer(sample_list1)
    analyzer2 = ListAnalyzer(sample_list2)
    print(analyzer1.find_first_value())
    print(analyzer2.find_first_value())