class ListAnalyzer:
    EMPTY_LIST_MESSAGE = "List is empty"

    def __init__(self, lst):
        self.lst = lst

    def find_first_value(self):
        if not self.lst:
            return None
        return self.lst[0]

if __name__ == '__main__':
    SAMPLE_LIST_1 = [10, 20, 30]
    SAMPLE_LIST_2 = []
    
    analyzer1 = ListAnalyzer(SAMPLE_LIST_1)
    analyzer2 = ListAnalyzer(SAMPLE_LIST_2)

    print(analyzer1.find_first_value())
    print(analyzer2.find_first_value() or ListAnalyzer.EMPTY_LIST_MESSAGE)