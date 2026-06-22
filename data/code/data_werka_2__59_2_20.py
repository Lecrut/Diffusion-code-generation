class SequenceAnalyzer:

    def get_middle(self, iterable):
        if not hasattr(iterable, '__iter__'):
            raise ValueError('Input must be an iterable')
        sorted_iterable = sorted(iterable)
        n = len(sorted_iterable)
        mid_index = n // 2
        if n % 2 == 0:
            return (sorted_iterable[mid_index - 1] + sorted_iterable[mid_index]) / 2
        else:
            return sorted_iterable[mid_index]
if __name__ == '__main__':
    analyzer = SequenceAnalyzer()
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    print(analyzer.get_middle(sample_list))
    sample_tuple = (8, 6, 7, 5, 3, 0, 9)
    print(analyzer.get_middle(sample_tuple))
    sample_string = 'hello'
    print(analyzer.get_middle(sample_string))