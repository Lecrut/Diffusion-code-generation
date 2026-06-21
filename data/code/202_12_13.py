class NumberAnalyzer:
    def get_maximum(self, data_list):
        if not data_list:
            raise ValueError("Input list cannot be empty")
        return max(map(float, data_list))

if __name__ == '__main__':
    analyzer = NumberAnalyzer()
    sample_data1 = [10, 5, 20.5, 8, 15]
    sample_data2 = [-5, -1.5, -10, -3]
    sample_data3 = [42.75]
    print(f"Maximum of {sample_data1}: {analyzer.get_maximum(sample_data1)}")
    print(f"Maximum of {sample_data2}: {analyzer.get_maximum(sample_data2)}")
    print(f"Maximum of {sample_data3}: {analyzer.get_maximum(sample_data3)}")