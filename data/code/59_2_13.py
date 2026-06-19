class SequenceAnalyzer:
    def get_middle(self, iterable):
        if not iterable:
            return None
        
        sorted_iterable = sorted(iterable)
        n = len(sorted_iterable)
        
        if n % 2 == 1:
            return sorted_iterable[n // 2]
        else:
            left_middle = sorted_iterable[n // 2 - 1]
            right_middle = sorted_iterable[n // 2]
            return (left_middle + right_middle) / 2

if __name__ == '__main__':
    analyzer = SequenceAnalyzer()
    sample_data = [10, 20, 30, 40, 50]
    print(analyzer.get_middle(sample_data))