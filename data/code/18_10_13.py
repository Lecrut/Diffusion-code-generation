class ListAnalyzer:
    def __init__(self, data):
        self.data = list(data)

    def get_middle(self):
        if not self.data:
            return None
        return self.data[len(self.data) // 2]

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [10, 20, 30, 40]
    single_list = [99]
    empty_list = []

    analyzer_odd = ListAnalyzer(odd_list)
    analyzer_even = ListAnalyzer(even_list)
    analyzer_single = ListAnalyzer(single_list)
    analyzer_empty = ListAnalyzer(empty_list)

    print(analyzer_odd.get_middle())
    print(analyzer_even.get_middle())
    print(analyzer_single.get_middle())
    print(analyzer_empty.get_middle())