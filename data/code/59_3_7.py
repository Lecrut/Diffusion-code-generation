class SequenceAnalyzer:
    def get_middle(self, data):
        sorted_data = sorted(list(data))
        n = len(sorted_data)
        if n == 0:
            return None
        elif n % 2 == 1:
            return sorted_data[n // 2]
        else:
            middle1 = sorted_data[n // 2 - 1]
            middle2 = sorted_data[n // 2]
            return (middle1 + middle2) / 2
if __name__ == '__main__':
    analyzer = SequenceAnalyzer()
    data1 = [1, 5, 2, 8, 3]
    result1 = analyzer.get_middle(data1)
    print(f"Data: {data1}, Middle: {result1}")
    data2 = [10, 20, 30, 40, 50]
    result2 = analyzer.get_middle(data2)
    print(f"Data: {data2}, Middle: {result2}")
    data3 = [1, 2, 3, 4]
    result3 = analyzer.get_middle(data3)
    print(f"Data: {data3}, Middle: {result3}")
    data4 = [1, 2, 3, 4, 5, 6]
    result4 = analyzer.get_middle(data4)
    print(f"Data: {data4}, Middle: {result4}")
    data5 = [10]
    result5 = analyzer.get_middle(data5)
    print(f"Data: {data5}, Middle: {result5}")
    data6 = []
    result6 = analyzer.get_middle(data6)
    print(f"Data: {data6}, Middle: {result6}")