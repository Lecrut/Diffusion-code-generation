class ListAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_middle_element(self):
        n = len(self.data)
        if n == 0:
            return None
        middle_index = n // 2
        return self.data[middle_index]

if __name__ == '__main__':
    sample_list_odd = [1, 5, 2, 8, 3]
    analyzer_odd = ListAnalyzer(sample_list_odd)
    result_odd = analyzer_odd.find_middle_element()
    print(result_odd)

    sample_list_even = [1, 5, 2, 8, 3, 9]
    analyzer_even = ListAnalyzer(sample_list_even)
    result_even = analyzer_even.find_middle_element()
    print(result_even)