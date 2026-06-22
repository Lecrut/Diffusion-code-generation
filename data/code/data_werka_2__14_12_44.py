class VolumeAnalyzer:

    def __init__(self, volume1, volume2):
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise ValueError('Both volumes must be numbers.')
        self.volume1 = volume1
        self.volume2 = volume2

    def get_comparison_result(self):
        if self.volume1 > self.volume2:
            return 'First volume is greater than the second.'
        elif self.volume1 < self.volume2:
            return 'First volume is less than the second.'
        else:
            return 'Both volumes are equal.'
if __name__ == '__main__':
    try:
        analyzer = VolumeAnalyzer(6.28318, 3.14159)
        print(analyzer.get_comparison_result())
        analyzer.volume1 = 2.71828
        print(analyzer.get_comparison_result())
        analyzer.volume1 = 3.14159
        print(analyzer.get_comparison_result())
    except ValueError as e:
        print(e)