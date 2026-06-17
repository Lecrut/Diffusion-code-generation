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
    sample_data = [10, 5, 20, 8, 15]
    result = analyzer.get_max(sample_data)
    print(result)
    sample_data_2 = [-5, -1, -10, -3]
    result_2 = analyzer.get_max(sample_data_2)
    print(result_2)
    empty_data = []
    try:
        analyzer.get_max(empty_data)
    except ValueError as e:
        print(e)