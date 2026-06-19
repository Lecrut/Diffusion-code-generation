class SequenceAnalyzer:
    def get_middle(self, data):
        if len(data) % 2 == 0:
            raise ValueError("List must have an odd length")
        sorted_data = sorted(data)
        return sorted_data[len(sorted_data) // 2]

if __name__ == '__main__':
    analyzer = SequenceAnalyzer()
    sample1 = [3, 1, 4, 1, 5]
    print(f"Data: {sample1}, Middle: {analyzer.get_middle(sample1)}")
    sample2 = [9, 8, 7, 6, 5]
    print(f"Data: {sample2}, Middle: {analyzer.get_middle(sample2)}")