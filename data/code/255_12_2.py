class DataAnalyzer:
    def get_max(self, data_list):
        if not data_list:
            raise ValueError("Input list cannot be empty")
        max_value = data_list[0]
        for item in data_list[1:]:
            if item > max_value:
                max_value = item
        return max_value
if __name__ == '__main__':
    analyzer = DataAnalyzer()
    sample_data_1 = [10, 5, 20, 8, 15]
    sample_data_2 = [-5, -1, -10, -3]
    sample_data_3 = [42]
    sample_data_4 = []
    print(f"Max of {sample_data_1}: {analyzer.get_max(sample_data_1)}")
    print(f"Max of {sample_data_2}: {analyzer.get_max(sample_data_2)}")
    print(f"Max of {sample_data_3}: {analyzer.get_max(sample_data_3)}")
    try:
        analyzer.get_max(sample_data_4)
    except ValueError as e:
        print(f"Error for empty list: {e}")