class ListAnalyzer:
    def find_largest(self, data):
        if not data:
            return None
        return max(data)

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [-10, -5, -20, -1]
    print(analyzer.find_largest(list1))
    print(analyzer.find_largest(list2))