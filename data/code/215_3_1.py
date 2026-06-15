class NumberAnalyzer:
    def get_largest(self, data_list):
        if not data_list:
            raise ValueError("Input list cannot be empty")
        largest = data_list[0]
        for number in data_list[1:]:
            if number > largest:
                largest = number
        return largest
if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    sample_data1 = [10, 5, 20, 8, 15]
    sample_data2 = [-5, -1, -10, -3]
    sample_data3 = [42]
    sample_data4 = []
    print(f"Largest in {sample_data1}: {analyzer.get_largest(sample_data1)}")
    print(f"Largest in {sample_data2}: {analyzer.get_largest(sample_data2)}")
    print(f"Largest in {sample_data3}: {analyzer.get_largest(sample_data3)}")
    try:
        analyzer.get_largest(sample_data4)
    except ValueError as e:
        print(f"Error for {sample_data4}: {e}")