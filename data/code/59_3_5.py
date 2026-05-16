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
    print(f"Data: {sample1}, Middle: {analyzer.get_middle(sample1)}")
    sample2 = [1, 2, 3, 4, 5]
    print(f"Data: {sample2}, Middle: {analyzer.get_middle(sample2)}")
    sample3 = [10, 20, 30, 40]
    print(f"Data: {sample3}, Middle: {analyzer.get_middle(sample3)}")
    sample4 = [1, 2, 3, 4]
    print(f"Data: {sample4}, Middle: {analyzer.get_middle(sample4)}")
    sample5 = [100]
    print(f"Data: {sample5}, Middle: {analyzer.get_middle(sample5)}")
    sample6 = []
    print(f"Data: {sample6}, Middle: {analyzer.get_middle(sample6)}")