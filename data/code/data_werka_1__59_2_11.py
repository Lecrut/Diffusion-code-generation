class SequenceAnalyzer:
    def get_middle(self, iterable):
        if not iterable:
            raise ValueError("Input is empty")
        
        sorted_iterable = sorted(iterable)
        n = len(sorted_iterable)
        
        if n % 2 == 1:
            middle_index = n // 2
            return sorted_iterable[middle_index]
        else:
            middle_left_index = n // 2 - 1
            middle_right_index = n // 2
            return (sorted_iterable[middle_left_index] + sorted_iterable[middle_right_index]) / 2

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2]
    analyzer = SequenceAnalyzer()
    print(analyzer.get_middle(sample_data))