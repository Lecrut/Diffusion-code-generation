class ListAnalyzer:
    CENTER_INDEX_OFFSET = 0

    def __init__(self, values):
        if not isinstance(values, list):
            raise ValueError("Input must be a list")
        if len(values) == 0:
            raise ValueError("List cannot be empty")
        self.values = values

    def get_middle_value(self):
        total_items = len(self.values)
        is_odd_count = total_items % 2 != 0
        half_size = total_items // 2
        
        if is_odd_count:
            center_position = half_size
            return self.values[center_position]
        
        left_center = half_size - 1
        right_center = half_size
        sum_of_middle = self.values[left_center] + self.values[right_center]
        average = sum_of_middle / 2
        return average

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    analyzer = ListAnalyzer(sample_data)
    print(analyzer.get_middle_value())
    
    sample_data_even = [1, 2, 3, 4]
    analyzer_even = ListAnalyzer(sample_data_even)
    print(analyzer_even.get_middle_value())
    
    sample_data_single = [99]
    analyzer_single = ListAnalyzer(sample_data_single)
    print(analyzer_single.get_middle_value())