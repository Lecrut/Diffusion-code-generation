class SequenceAnalyzer:
    def get_middle(self, iterable):
        if not iterable:
            raise ValueError("The input iterable is empty")
        
        sorted_iterable = sorted(iterable)
        length = len(sorted_iterable)
        middle_index = length // 2
        
        if length % 2 == 0:
            return (sorted_iterable[middle_index - 1] + sorted_iterable[middle_index]) / 2
        else:
            return sorted_iterable[middle_index]

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2]
    analyzer = SequenceAnalyzer()
    print(analyzer.get_middle(sample_data))