class ListAnalyzer:
    def get_largest(self, data_list):
        if not data_list:
            raise ValueError("Input list cannot be empty")
        largest = data_list[0]
        for item in data_list[1:]:
            if item > largest:
                largest = item
        return largest
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_data1 = [10, 5, 20, 8, 15]
    sample_data2 = [-5, -1, -10, -3]
    sample_data3 = [42]
    sample_data4 = []
    result1 = analyzer.get_largest(sample_data1)
    print(f"Largest in {sample_data1}: {result1}")
    result2 = analyzer.get_largest(sample_data2)
    print(f"Largest in {sample_data2}: {result2}")
    result3 = analyzer.get_largest(sample_data3)
    print(f"Largest in {sample_data3}: {result3}")
    try:
        analyzer.get_largest(sample_data4)
    except ValueError as e:
        print(f"Error for {sample_data4}: {e}")