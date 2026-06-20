class ListAnalyzer:
    def get_middle_value(self, data):
        if not data:
            return None
        n = len(data)
        middle_index = n // 2
        return data[middle_index]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50, 60]
    print(f"Middle of {list1}: {analyzer.get_middle_value(list1)}")
    print(f"Middle of {list2}: {analyzer.get_middle_value(list2)}")