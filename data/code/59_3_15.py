class SequenceAnalyzer:
    def get_middle(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        return sorted_data[n // 2] if n % 2 == 1 else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

if __name__ == '__main__':
    analyzer = SequenceAnalyzer()
    sample1 = [3, 1, 4, 1, 5]
    print(f"Data: {sample1}, Middle: {analyzer.get_middle(sample1)}")
    sample2 = [9, 8, 7, 6, 5, 4]
    print(f"Data: {sample2}, Middle: {analyzer.get_middle(sample2)}")