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
    sample_data_1 = [10, 5, 20, 8, 15]
    sample_data_2 = [-5, -1, -10, -3]
    sample_data_3 = [42]
    sample_data_4 = []
    result_1 = analyzer.get_largest(sample_data_1)
    print(f"Largest in {sample_data_1}: {result_1}")
    result_2 = analyzer.get_largest(sample_data_2)
    print(f"Largest in {sample_data_2}: {result_2}")
    result_3 = analyzer.get_largest(sample_data_3)
    print(f"Largest in {sample_data_3}: {result_3}")
    try:
        analyzer.get_largest(sample_data_4)
    except ValueError as e:
        print(f"Error for {sample_data_4}: {e}")