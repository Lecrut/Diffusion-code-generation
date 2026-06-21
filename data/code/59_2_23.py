class SequenceAnalyzer:
    def get_middle(self, iterable):
        if not hasattr(iterable, '__iter__'):
            raise ValueError("The input is not an iterable")
        
        sorted_iterable = sorted(iterable)
        length = len(sorted_iterable)
        
        if length == 0:
            raise ValueError("The iterable is empty")
        
        mid_index = length // 2
        if length % 2 == 0:
            return (sorted_iterable[mid_index - 1] + sorted_iterable[mid_index]) / 2
        else:
            return sorted_iterable[mid_index]

if __name__ == '__main__':
    analyzer = SequenceAnalyzer()
    sample_list = [7, 3, 5, 9, 1]
    print(analyzer.get_middle(sample_list))