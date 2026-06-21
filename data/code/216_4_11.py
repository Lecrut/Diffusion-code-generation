class ListAnalyzer:

    def find_middle(self, data):
        n = len(data)
        if n == 0:
            return None
        sorted_data = sorted(data)
        middle_index = n // 2
        if n % 2 != 0:
            return sorted_data[middle_index]
        else:
            return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    list1 = [3, 1, 4, 1, 5, 9, 2]
    print(analyzer.find_middle(list1))
    list2 = []
    print(analyzer.find_middle(list2))
    list3 = [7]
    print(analyzer.find_middle(list3))