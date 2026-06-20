class ListAnalyzer:
    def get_middle_value(self, data):
        n = len(data)
        if n == 0:
            return None
        middle_index = n // 2
        return data[middle_index]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    list1 = [1, 2, 3, 4, 5]
    print(f"Middle of {list1}: {analyzer.get_middle_value(list1)}")