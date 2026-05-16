class SequenceAnalyzer:
    def get_middle(self, data):
        sorted_data = sorted(list(data))
        n = len(sorted_data)
        if n == 0:
            return None
        else:
            middle_index = n // 2
            if n % 2 == 1:
                return sorted_data[middle_index]
            else:
                return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2
if __name__ == '__main__':
    analyzer = SequenceAnalyzer()
    sample1 = [1, 5, 2, 8, 3]
    result1 = analyzer.get_middle(sample1)
    print(f"Sample 1: {sample1}")
    print(f"Middle element (average): {result1}")
    sample2 = [10, 20, 30, 40]
    result2 = analyzer.get_middle(sample2)
    print(f"Sample 2: {sample2}")
    print(f"Middle element (average): {result2}")
    sample3 = [1, 2, 3, 4, 5, 6]
    result3 = analyzer.get_middle(sample3)
    print(f"Sample 3: {sample3}")
    print(f"Middle element (median): {result3}")
    sample4 = [7]
    result4 = analyzer.get_middle(sample4)
    print(f"Sample 4: {sample4}")
    print(f"Middle element (median): {result4}")
    sample5 = []
    result5 = analyzer.get_middle(sample5)
    print(f"Sample 5: {sample5}")
    print(f"Middle element (median): {result5}")