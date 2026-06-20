class ListAnalyzer:
    def get_middle_value(self, data):
        n = len(data)
        if n == 0:
            return None
        middle_index = n // 2
        return data[middle_index]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    list1 = [7, 8, 9, 10, 11]
    list2 = [15, 25, 35, 45, 55, 65]
    print(f"Middle of {list1}: {analyzer.get_middle_value(list1)}")
    print(f"Middle of {list2}: {analyzer.get_middle_value(list2)}")