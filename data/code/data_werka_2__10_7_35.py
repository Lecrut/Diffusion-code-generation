class TemperatureAnalyzer:
    DEFAULT_TOLERANCE = 1

    def __init__(self, tolerance=DEFAULT_TOLERANCE):
        self.tolerance = tolerance

    def compare(self, temp1, temp2):
        if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
            raise ValueError('Both temperature values must be numbers.')
        return abs(temp1 - temp2) <= self.tolerance
if __name__ == '__main__':
    sample_temp1 = 18.0
    sample_temp2 = 19.5
    analyzer = TemperatureAnalyzer()
    result_within_tolerance = analyzer.compare(sample_temp1, sample_temp2)
    print('Are temperatures within tolerance?', result_within_tolerance)
    analyzer.tolerance = 2
    result_with_new_tolerance = analyzer.compare(sample_temp1, sample_temp2)
    print('Are temperatures within new tolerance?', result_with_new_tolerance)