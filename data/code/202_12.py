class NumberAnalyzer:
    def get_maximum(self, data_list):
        if not data_list:
            raise ValueError("Input list cannot be empty")
        maximum = data_list[0]
        for number in data_list:
            if number > maximum:
                maximum = number
        return maximum
if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    sample_data1 = [10, 5, 20, 8, 15]
    sample_data2 = [-5, -1, -10, -3]
    sample_data3 = [42]
    sample_data4 = []
    result1 = analyzer.get_maximum(sample_data1)
    print(f"Maximum of {sample_data1}: {result1}")
    result2 = analyzer.get_maximum(sample_data2)
    print(f"Maximum of {sample_data2}: {result2}")
    result3 = analyzer.get_maximum(sample_data3)
    print(f"Maximum of {sample_data3}: {result3}")
    try:
        analyzer.get_maximum(sample_data4)
    except ValueError as e:
        print(f"Error for {sample_data4}: {e}")