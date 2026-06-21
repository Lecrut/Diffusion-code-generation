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
    sample_data1 = [4, 8, 15, 16, 23, 42]
    print(f"Largest in {sample_data1}: {analyzer.get_largest(sample_data1)}")