class ListAnalyzer:
    def __init__(self, values):
        if not isinstance(values, list):
            raise ValueError("Input must be a list")
        self.values = values

    def get_middle_value(self):
        count = len(self.values)
        if count == 0:
            return None
        if count % 2 == 1:
            center_idx = count // 2
            return self.values[center_idx]
        else:
            left_idx = count // 2 - 1
            right_idx = count // 2
            left_val = self.values[left_idx]
            right_val = self.values[right_idx]
            return (left_val + right_val) / 2

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60]
    analyzer = ListAnalyzer(sample_data)
    result = analyzer.get_middle_value()
    print(result)
    
    sample_data_odd = [1, 2, 3, 4, 5]
    analyzer_odd = ListAnalyzer(sample_data_odd)
    result_odd = analyzer_odd.get_middle_value()
    print(result_odd)