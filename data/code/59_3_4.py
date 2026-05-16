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
    sample1 = [1, 5, 2, 8, 3]
    result1 = analyzer.get_middle(sample1)
    print(f"Sequence: {sample1}, Middle: {result1}")
    sample2 = [1, 2, 3, 4, 5]
    result2 = analyzer.get_middle(sample2)
    print(f"Sequence: {sample2}, Middle: {result2}")
    sample3 = [1, 2, 3, 4]
    result3 = analyzer.get_middle(sample3)
    print(f"Sequence: {sample3}, Middle: {result3}")
    sample4 = [10, 20, 30, 40, 50, 60]
    result4 = analyzer.get_middle(sample4)
    print(f"Sequence: {sample4}, Middle: {result4}")
    sample5 = [7]
    result5 = analyzer.get_middle(sample5)
    print(f"Sequence: {sample5}, Middle: {result5}")
    sample6 = []
    result6 = analyzer.get_middle(sample6)
    print(f"Sequence: {sample6}, Middle: {result6}")