class SequenceAnalyzer:
    def get_middle(self, iterable):
        sorted_iterable = sorted(iterable)
        length = len(sorted_iterable)
        if length == 0:
            raise ValueError("The input iterable is empty")
        middle_index = length // 2
        if length % 2 == 0:
            return (sorted_iterable[middle_index - 1] + sorted_iterable[middle_index]) / 2
        else:
            return sorted_iterable[middle_index]

if __name__ == '__main__':
    analyzer = SequenceAnalyzer()
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    print(analyzer.get_middle(sample_list))