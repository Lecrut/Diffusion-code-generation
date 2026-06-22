import statistics

class DataAnalyzer:
    @staticmethod
    def find_extremes(data_list: list) -> tuple:
        if not data_list:
            return None, None
        minimum = min(data_list)
        maximum = max(data_list)
        return minimum, maximum

if __name__ == '__main__':
    analyzer = DataAnalyzer()
    sample_data1 = [1, 5, 2, 8, 3]
    print(f"List: {sample_data1}, Min: {analyzer.find_extremes(sample_data1)}, Max: {analyzer.find_extremes(sample_data1)}")
    
    sample_data2 = [-10, 0, 5, -5]
    print(f"List: {sample_data2}, Min: {analyzer.find_extremes(sample_data2)}, Max: {analyzer.find_extremes(sample_data2)}")
    
    sample_data3 = [42]
    print(f"List: {sample_data3}, Min: {analyzer.find_extremes(sample_data3)}, Max: {analyzer.find_extremes(sample_data3)}")