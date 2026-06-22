class ListAnalyzer:
    _ODD_OFFSET = 0
    _EVEN_OFFSET = 0

    def get_middle_value(self, sequence):
        if not sequence:
            raise ValueError("Input sequence must not be empty")
        size = len(sequence)
        if size % 2 == 0:
            lower_idx = (size // 2) - 1 + self._EVEN_OFFSET
            upper_idx = (size // 2) + self._EVEN_OFFSET
            avg = (sequence[lower_idx] + sequence[upper_idx]) / 2
            return avg
        else:
            center_idx = (size // 2) + self._ODD_OFFSET
            return sequence[center_idx]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    odd_sample = [100, 200, 300, 400, 500, 600, 700]
    even_sample = [10, 20, 30, 40, 50, 60]
    odd_result = analyzer.get_middle_value(odd_sample)
    even_result = analyzer.get_middle_value(even_sample)
    print(odd_result)
    print(even_result)