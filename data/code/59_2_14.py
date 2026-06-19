class SequenceAnalyzer:
    @staticmethod
    def get_middle(iterable):
        sorted_iterable = sorted(iterable)
        n = len(sorted_iterable)
        if n % 2 == 1:
            return sorted_iterable[n // 2]
        else:
            middle_left_index = n // 2 - 1
            middle_right_index = n // 2
            return (sorted_iterable[middle_left_index] + sorted_iterable[middle_right_index]) / 2

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2]
    analyzer = SequenceAnalyzer()
    middle_value = analyzer.get_middle(sample_values)
    print(middle_value)