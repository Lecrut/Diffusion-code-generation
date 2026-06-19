class SequenceAnalyzer:
    def get_middle(self, iterable):
        if not iterable:
            return None
        
        sorted_iterable = sorted(iterable)
        n = len(sorted_iterable)
        
        if n % 2 == 1:
            return sorted_iterable[n // 2]
        else:
            return (sorted_iterable[n // 2 - 1] + sorted_iterable[n // 2]) / 2

if __name__ == '__main__':
    analyzer = SequenceAnalyzer()
    sample_data = [3, 1, 4, 1, 5, 9, 2]
    print(analyzer.get_middle(sample_data))